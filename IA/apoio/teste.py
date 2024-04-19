#from read_process_ia import ProcessedImage
from dataclasses import dataclass
from pathlib import Path
import json
import os

class SampleTableElements:
    def __init__(self):
        self.file_count_dict = {}

    @staticmethod
    def qtd_foliolos(json_file: Path) -> int:
        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)
        count = len(data)
        opened_file.close()  # Close the file after reading
        return count
    
    def spider_mite_average_leaf(self, json_file: str) -> float:  # images_list: list[ProcessedImage] 
        spider_mite_total = 0
        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)

        leaf_total = self.qtd_foliolos(json_file)
        for item in data:
            rajado = item.get("rajado")
            spider_mite_total += rajado
        average = spider_mite_total / leaf_total
        opened_file.close()
        self.file_count_dict[json_file]["media_rajado_foliolo"] = average
        return average

    def count_elements(self, json_file: Path):

        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)
        total_foliolos = self.qtd_foliolos(json_file)  # Total folíolos for this file
        for item in data:
            rajado = int(item.get("rajado"))
            macropilis = int(item.get("macropilis"))
            californicus = int(item.get("californicus"))
            if macropilis == 0 and californicus == 0 and rajado == 0:
                self.increment_count(json_file.name, "without_predator_without_mite", total_foliolos)
            elif (macropilis != 0 or californicus != 0) and rajado != 0:
                self.increment_count(json_file.name, "with_predator_with_mite", total_foliolos)
            elif (macropilis != 0 or californicus != 0) and rajado == 0:
                self.increment_count(json_file.name, "with_predator_without_mite", total_foliolos)
            elif (macropilis == 0 and californicus == 0) and rajado != 0:
                if rajado > 10:
                    self.increment_count(json_file.name, "moreThan_ten_mite", total_foliolos)
                elif 6 <= rajado <= 9:
                    self.increment_count(json_file.name, "six_to_nine_mite", total_foliolos)
                elif 1 <= rajado <= 5:
                    self.increment_count(json_file.name, "one_to_five_mite", total_foliolos)
        self.final_classification()
        opened_file.close()  # Close the file after reading

    def increment_count(self, file_name: str, key: str, total_foliolos: int):
        if file_name not in self.file_count_dict:
            self.file_count_dict[file_name] = {}
        if key not in self.file_count_dict[file_name]:
            self.file_count_dict[file_name][key] = 0
        self.file_count_dict[file_name][key] += 1
        # Calculate and store percentage
        percentage_key = f"{key}_percentage"
        self.file_count_dict[file_name][percentage_key] = (
            self.file_count_dict[file_name][key] / total_foliolos
        )

        # Remove original count key and value
        del self.file_count_dict[file_name][key]

        self.file_count_dict[file_name]["qtd_total"] = total_foliolos
        self.spider_mite_average_leaf(file_name)
        self.increment_keys()

    def increment_keys(self):
        l = []
        keys = ["without_predator_without_mite_percentage", "with_predator_with_mite_percentage", "with_predator_without_mite_percentage", "moreThan_ten_mite_percentage", "six_to_nine_mite_percentage", "one_to_five_mite_percentage"]
        for file_name, counts in self.file_count_dict.items():
            for key, value in counts.items():
                l.append(key)
            for i in keys:
                if i not in l:
                    self.file_count_dict[file_name][i] = 0
            l = []

    def final_classification(self) -> str:
        max_priority_percentage = 0.3  # Threshold for prioritized classifications
        prioritized_keys = ["moreThan_ten_mite_percentage", "six_to_nine_mite_percentage", "one_to_five_mite_percentage"]
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

        self.file_count_dict[file_name]["final_class"] = final_class  # Save final_class in dict
        self.suggested_action(file_name,final_class)
        self.reset_final_class()
        return final_class

    def suggested_action(self, file_name: str, final_class: str) -> str:
        suggested_action = ""
        if final_class == "moreThan_ten_mite":
            suggested_action = "Chamar o Victor!"
        elif final_class == "six_to_nine_mite":
            suggested_action = "Soltar ácaro predador!"
        elif final_class == "one_to_five_mite":
            suggested_action = "Jogar água!"
        else:
            suggested_action = "Não fazer nada!"

        self.file_count_dict[file_name]["suggested_action"] = suggested_action
        self.reset_suggested_action()  # Reset suggested_action after processing
        return suggested_action
    
    def reset_final_class(self):
        final_class = ""  # Reset final_class to an empty string

    def reset_suggested_action(self):
        suggested_action = ""  # Reset suggested_action to an empty string

    def teste(self):
        for file_name, counts in self.file_count_dict.items():
            print(file_name)
            for key, value in counts.items():
                print(f"{key}: {value}")
            del sample_table.file_count_dict[file_name]

# Bloco de Teste
if __name__ == "__main__":
    # Testando a classe SampleTableElements
    sample_table = SampleTableElements()
    sample_table.count_elements(Path("fidelis@gmail.com_13_03042024_145758"))
    sample_table.count_elements(Path("wilsiman.evangelista.ifes@gmail.com_10_20240129_125740"))
    # Exibindo o dicionário de contagem
    print("Contagem de Elementos e Porcentagem por Arquivo:")
    for file_name, counts in sample_table.file_count_dict.items():
        print(f"\n\nArquivo: {file_name}")
        for key, value in counts.items():
            print(f"{key}: {value}")

    # Exibindo a classificação final e ação sugerida
    for file_name in sample_table.file_count_dict:
        final_class = sample_table.file_count_dict[file_name]["final_class"]
        suggested_action = sample_table.file_count_dict[file_name]["suggested_action"]
        print(f"\n\nArquivo: {file_name}")
        print(f"Classificação Final: {final_class}")
        print(f"Ação Sugerida: {suggested_action}")
        print()
    print("\nDicionário Atualizado:\n")
    print(sample_table.file_count_dict)
    
    #sample_table.increment_keys()
    print()
    print()
    print()

    sample_table.teste()

    print()
    print()
    print()

    print("\nDicionário Atualizado:\n")
    print(sample_table.file_count_dict)