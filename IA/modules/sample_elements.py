from __init__ import JSONS_PATH
from pathlib import Path
import json

class SampleTableElements:
    """Class responsible for creating elements for insertion into the sampling table"""
    def __init__(self):
        self.file_count_dict = {}

    @staticmethod
    def qtd_foliolos(json_file: Path) -> int:
        """
        Feature: Function responsible for counting the number of images present in the appropriate folder that corresponds to the number of leaves.

        @param json_file: Json directory path.

        @return: int (number of leaves)
        """

        opened_file = open(f"{JSONS_PATH}/{json_file}.json")
        data = json.load(opened_file)
        count = len(data)
        opened_file.close()  # Close the file after reading
        return count
    
    def spider_mite_average_leaf(self, json_file: str) -> float:
        """
        Feature: Function responsible for calculating the average number of spider mites per leaf.

        @param json_file: Json directory path.

        @return: float (average number of spider mites per leaf).
        """

        spider_mite_total = 0
        opened_file = open(f"{JSONS_PATH}/{json_file}.json")
        data = json.load(opened_file)

        leaf_total = self.qtd_foliolos(json_file)
        for item in data:
            rajado = item.get("rajado")
            spider_mite_total += rajado
        average = spider_mite_total / leaf_total
        opened_file.close()
        self.file_count_dict[json_file]["media_rajado_foliolo"] = average
        return average

    def count_elements(self, json_file: Path) -> None:
        """
        Feature: Function responsible for checking how many mites of each type are on each leaf and then calling a function that increases one unit in the counter referring to the rule that each leaf fits.

        @param json_file: Json directory path.

        @return: None.
        """

        opened_file = open(f"{JSONS_PATH}/{json_file}.json")
        data = json.load(opened_file)
        total_foliolos = SampleTableElements.qtd_foliolos(json_file)  # Total folíolos for this file
        
        for item in data:
            rajado = int(item.get("rajado"))
            macropilis = int(item.get("macropilis"))
            californicus = int(item.get("californicus"))
            if macropilis == 0 and californicus == 0 and rajado == 0:
                self.increment_count(json_file.name, "sem_predador_sem_rajado", total_foliolos)
            elif (macropilis > 0 or californicus > 0) and rajado > 0:
                self.increment_count(json_file.name, "com_predador_com_rajado", total_foliolos)
            elif (macropilis != 0 or californicus != 0) and rajado == 0:
                self.increment_count(json_file.name, "com_predador_sem_rajado", total_foliolos)
            elif (macropilis == 0 and californicus == 0) and rajado != 0:
                if rajado > 10:
                    self.increment_count(json_file.name, "mais_dez_rajado", total_foliolos)
                elif 6 <= rajado <= 9:
                    self.increment_count(json_file.name, "seis_a_nove_rajado", total_foliolos)
                elif 1 <= rajado <= 5:
                    self.increment_count(json_file.name, "um_a_cinco_rajado", total_foliolos)
        self.final_classification()
        opened_file.close()  # Close the file after reading

    def increment_count(self, file_name: str, key: str, total_foliolos: int):
        """
        Feature: Function responsible for increasing one unit in the counter according to the rule that each sheet fits.

        @params: 
            file_name: file name;
            

        @return: None.
        """

        if file_name not in self.file_count_dict:
            self.file_count_dict[file_name] = {}
        if key not in self.file_count_dict[file_name]:
            self.file_count_dict[file_name][key] = 0
        self.file_count_dict[file_name][key] += 1
        # Calculate and store percentage
        percentage_key = f"{key}_percentage"
        self.file_count_dict[file_name][percentage_key] = (
            self.file_count_dict[file_name][key] / total_foliolos * 100
        )

        # Remove original count key and value
        #del self.file_count_dict[file_name][key]

        self.file_count_dict[file_name]["qtd_total"] = total_foliolos
        self.spider_mite_average_leaf(file_name)
        self.increment_keys()

    def increment_keys(self):
        l = []
        keys = ["sem_predador_sem_rajado_percentage", "com_predador_com_rajado_percentage", "com_predador_sem_rajado_percentage", "mais_dez_rajado_percentage", "seis_a_nove_rajado_percentage", "um_a_cinco_rajado_percentage"]
        for file_name, counts in self.file_count_dict.items():
            for key, value in counts.items():
                l.append(key)
            for i in keys:
                if i not in l:
                    self.file_count_dict[file_name][i] = 0
            l = []

    def final_classification(self) -> str:
        max_priority_percentage = 30  # Threshold for prioritized classifications
        prioritized_keys = ["mais_dez_rajado_percentage", "seis_a_nove_rajado_percentage", "um_a_cinco_rajado_percentage"]
        max_percentage = 0
        final_class = ""

        for file_name, counts in self.file_count_dict.items():
            for key, value in counts.items():
                if key in prioritized_keys and value >= max_priority_percentage:
                    final_class = key.replace("_percentage", "")  # Return prioritized classification
                    break
                elif key.endswith("_percentage") and value > max_percentage:
                    max_percentage = value
                    final_class = key.replace("_percentage", "")

        self.file_count_dict[file_name]["classe_final"] = final_class  # Save final_class in dict
        self.suggested_action(file_name,final_class)
        self.reset_final_class()
        return final_class

    def suggested_action(self, file_name: str, final_class: str) -> str:
        suggested_action = ""
        if final_class == "mais_dez_rajado":
            suggested_action = "Pulverizar Químico."
        elif final_class == "seis_a_nove_rajado":
            suggested_action = "Chamar Entomologista."
        elif final_class == "um_a_cinco_rajado":
            suggested_action = "Liberar 2 predadores por planta."
        else:
            suggested_action = "Apenas manter observação."

        self.file_count_dict[file_name]["acao_sugerida"] = suggested_action

        self.reset_suggested_action()  # Reset suggested_action after processing
        return suggested_action
    
    def reset_final_class(self):
        final_class = ""  # Reset final_class to an empty string

    def reset_suggested_action(self):
        suggested_action = ""  # Reset suggested_action to an empty string
