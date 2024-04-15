from modules.read_process_ia import ProcessedImage
from dataclasses import dataclass
from pathlib import Path
import json
import os

class SampleTableElements:
    def __init__(self) -> None:
        self.leafs_count = {
            "more_than_ten": 0
        }
    
    def reset_leafs_count(self):
        for key in self.leafs_count:
            self.leafs_count[key] = 0

    def count_leafs(self, leaf_name, confirmation):
        if confirmation:
            self.leafs_count[leaf_name] += 1
    
    def count_leafs_as_percent(self, leaf_name, leaf_total):
        return self.leafs_count[leaf_name]/leaf_total

    '''
    @staticmethod
    def qtd_foliolos(json_file: Path) -> int:
        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)
        return len(data)

    @staticmethod
    def spider_mite_average_leaf(json_file: Path, leaf_total: int) -> float:  # images_list: list[ProcessedImage] 
        spider_mite_total: int = 0
        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)
        for itens in data:
            rajado = itens.get("rajado")
            spider_mite_total += rajado
        average = spider_mite_total/leaf_total
        spider_mite_total = 0
        return average
        

    @staticmethod
    def decision_what_case_is(json_file: Path, leaf_total: int):
        opened_file = open(f"amostras\\{json_file}.json")
        data = json.load(opened_file)
        for itens in data:
            rajado = int(itens.get("rajado"))
            macropilis = int(itens.get("macropilis"))
            californicus = int(itens.get("californicus"))
            if(macropilis == 0 and californicus == 0 and rajado == 0):
                SampleTableElements.without_predator_without_mite(confirmation=True, leaf_total=leaf_total)
            elif((macropilis != 0 or californicus != 0) and rajado != 0):
                SampleTableElements.with_predator_with_mite(confirmation=True,leaf_total=leaf_total)
            elif((macropilis != 0 or californicus != 0) and rajado == 0):
                SampleTableElements.with_predator_without_mite(confirmation=True,leaf_total=leaf_total)
            elif((macropilis == 0 and californicus == 0) and rajado != 0):
                if(rajado>10):
                    SampleTableElements.moreThan_ten_mite(confirmation=True,leaf_total=leaf_total)
                elif(rajado>=6 and rajado<=9):
                    SampleTableElements.six_to_nine_mite(confirmation=True,leaf_total=leaf_total)
                elif(rajado>=1 and rajado<=5):
                    SampleTableElements.one_to_five_mite(confirmation=True,leaf_total=leaf_total)


    @staticmethod
    def without_predator_without_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total

    @staticmethod
    def with_predator_with_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total

    @staticmethod
    def with_predator_without_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total


    @staticmethod
    def one_to_five_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total

    @staticmethod
    def six_to_nine_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total

    @staticmethod
    def moreThan_ten_mite(confirmation: bool, leaf_total: int) -> float:
        number_leaf = 0
        if confirmation:
            number_leaf += 1
        return number_leaf/leaf_total

    

    def final_classification() -> str:
        pass

    def suggested_action() -> str:
        pass
'''
if __name__ == "__main__":
    sample_table_elements = SampleTableElements()
    sample_table_elements.count_leafs("more_than_ten", True)

    print(sample_table_elements.leafs_count)