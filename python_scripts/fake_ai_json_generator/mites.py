import random
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Mite(ABC):
    def __init__(self, current_population: int, current_management_technique_id: str):
        self.id : int
        self.relation_management_techniques_id: dict
        self.gene_varibility_modifyer: float
        self.default_grow_rate: float

        self.current_population = current_population
        self.current_management_technique_id = current_management_technique_id

    # TODO: implementate a decorator
    def variate_resistance_to_technique(self, management_technique_key: str, resistance_modifyer: float):
        if management_technique_key[0] in "Qq":
            data_want = self.relation_management_techniques_id[management_technique_key]
            data_want[0] += resistance_modifyer
            
            if data_want[0] > 1: data_want[0] = 1
            
            elif data_want[0] < 0: data_want[0] = 0
        else:
            self.relation_management_techniques_id[management_technique_key] += resistance_modifyer
            
            if self.relation_management_techniques_id[management_technique_key] > 1:
                self.relation_management_techniques_id[management_technique_key] = 1
            elif self.relation_management_techniques_id[management_technique_key] < 0:
                self.relation_management_techniques_id[management_technique_key] = 0

    def variate_resistance_to_active_priciple(self, active_principle: str, resistance_modifyer: float):
        for key in self.relation_management_techniques_id.keys():
            if key[0] in "Qq":
                if self.relation_management_techniques_id[key][1] == active_principle:
                    self.relation_management_techniques_id[key][0] += resistance_modifyer

    def evolution(self):
        # Variate the mite resistance to techniques
        for management_technique in self.relation_management_techniques_id.keys():
            if management_technique[0] in "Qq":
                if management_technique == self.current_management_technique_id:
                    resistance_modifyer = random.uniform(0, self.gene_varibility_modifyer)
                    priciple_active_modifyer = random.uniform(0, self.gene_varibility_modifyer)
                    self.variate_resistance_to_active_priciple(self.relation_management_techniques_id[management_technique][1], priciple_active_modifyer)
                else:
                    resistance_modifyer = random.uniform(-self.gene_varibility_modifyer, self.gene_varibility_modifyer)
            
                self.variate_resistance_to_technique(management_technique, resistance_modifyer)

        # Variate the genetic variability
        self.gene_varibility_modifyer += random.uniform(-0.001, 0.001)

        # Variate the population grow rate
        self.default_grow_rate += random.uniform(-0.001, 0.001)
    
    def next_population(self, other_mites_modifyer: float):
        if self.current_management_technique_id[0] in "Qq":
            new_grow_rate = self.default_grow_rate * self.relation_management_techniques_id[self.current_management_technique_id][0]
        else:
            new_grow_rate = self.default_grow_rate * self.relation_management_techniques_id[self.current_management_technique_id]

        next_mite_population = int(new_grow_rate * self.current_population * other_mites_modifyer)
        if next_mite_population < 0:
            next_mite_population = 0

        return next_mite_population
    
    @abstractmethod
    def pass_life_cycle(self):
        pass

    @staticmethod
    @abstractmethod
    def life_cycle_time() -> int:
        """
        Time in days
        """
        pass


class SpiderMite(Mite):
    def __init__(self, current_mite_population: int = 0, current_technique_id: str = ""):
        Mite.__init__(self, current_mite_population, current_technique_id)

        self.id = 1 

        self.default_grow_rate = 1 + random.uniform(0.1, 0.3)
        self.gene_varibility_modifyer = random.uniform(0.002, 0.02)


        # {management_techniques_id: [modifyer, active_principle]} -> modifier > 1 => grow mite population; modifyer < 1 => reduce mite population; and modifyer = 1 => stable mit population
        # 0.9 very weak; 0.8 weak; 0.7 medium; 0.6 strong; 0.5 very strong
        self.relation_management_techniques_id = {
            "q1": [0.9, "pa1"],
            "q2": [0.8, "pa1"],
            "q3": [0.7, "pa2"],
            "q4": [0.6, "pa3"],
            "q5": [0.5, "pa4"]
        }

    def pass_life_cycle(self, other_mites_modifyer):
        self.current_population = self.next_population(other_mites_modifyer=other_mites_modifyer)
        self.evolution()
    
    def influance_in_predatory_mite_populatio(self, current_predatory_mite_population: int, predatory_mite_comilance_rate: int) -> float:
        spider_mite_per_predator = self.current_population / current_predatory_mite_population
        
        if spider_mite_per_predator > predatory_mite_comilance_rate:
            return random.uniform(1.1, 1.2)
        elif spider_mite_per_predator > predatory_mite_comilance_rate - 1:
            return 1
        elif spider_mite_per_predator > predatory_mite_comilance_rate - 2:
            return random.uniform(0.8, 0.9)
        else:
            return random.uniform(0.1, 0.2)
    
    @staticmethod
    def life_cycle_time() -> int:
        return 14


class PredatoryMite(Mite):
    def __init__(self, current_mite_population: int = 0, current_technique_id: str = ""):
        Mite.__init__(self, current_mite_population, current_technique_id)

        self.id = 1 

        self.default_grow_rate = 1 + random.uniform(0.1, 0.3)
        self.gene_varibility_modifyer = random.uniform(0.002, 0.02)


        # {management_techniques_id: [modifyer, active_principle]} -> modifier > 1 => grow mite population; modifyer < 1 => reduce mite population; and modifyer = 1 => stable mit population
        # 0.9 very weak; 0.8 weak; 0.7 medium; 0.6 strong; 0.5 very strong
        self.relation_management_techniques_id = {
            "q1": [1, "pa1"],
            "q2": [1, "pa1"],
            "q3": [0.7, "pa2"],
            "q4": [0.9, "pa3"],
            "q5": [0.9, "pa4"]
        }
        self.comilance_rate = 5

    def pass_life_cycle(self, other_mites_modifyer):
        self.current_population = self.next_population(other_mites_modifyer=other_mites_modifyer)
        self.evolution()
    
    def influance_in_spider_mite_populatio(self, current_spider_mite_population: int) -> float:
        spider_mite_eaten = self.current_population * self.comilance_rate
        influence = 1 - spider_mite_eaten / current_spider_mite_population
        return influence

    def sudlen_death(self):
        self.current_population = 0

    @staticmethod
    def life_cycle_time() -> int:
        return 14


# TODO: integrate this class
class GeneralisPredatoryMite(Mite):
    def __init__(self, current_mite_population: int = 0, current_technique_id: str = ""):
        Mite.__init__(self, current_mite_population, current_technique_id)

        self.id = 1 

        self.default_grow_rate = 1 + random.uniform(0.1, 0.3)
        self.gene_varibility_modifyer = random.uniform(0.002, 0.02)


        # {management_techniques_id: [modifyer, active_principle]} -> modifier > 1 => grow mite population; modifyer < 1 => reduce mite population; and modifyer = 1 => stable mit population
        # 0.9 very weak; 0.8 weak; 0.7 medium; 0.6 strong; 0.5 very strong
        self.relation_management_techniques_id = {
            "q1": [0.9, "pa1"],
            "q2": [0.8, "pa1"],
            "q3": [0.7, "pa2"],
            "q4": [0.6, "pa3"],
            "q5": [0.5, "pa4"]
        }
        self.biological_controls_techiniques_id = ()

    def pass_life_cycle(self, other_mites_modifyer):
        self.current_population = self.next_population(other_mites_modifyer=other_mites_modifyer)
        self.evolution()
    
    @staticmethod
    def life_cycle_time() -> int:
        return 14


def main():
    spider_mite = SpiderMite(500, "q1")
    predator_mite = PredatoryMite(500, "q1")

    for i in range(1, 6):
        spider_mite.current_population = 500
        spider_mite.default_grow_rate = 1.3
        spider_mite.current_management_technique_id = f"q{i}"
        predator_mite.current_population = 80
        predator_mite.default_grow_rate = 1.3
        predator_mite.current_management_technique_id = f"q{i}"
        
        print()
        population_influence = ["spider mite in predator mite", "predator mite in spider mite"]
        for i in range(3):
            population_influence[0] = spider_mite.influance_in_predatory_mite_populatio(predator_mite.current_population, predator_mite.comilance_rate)
            
            if spider_mite.current_population > 0:
                population_influence[1] = predator_mite.influance_in_spider_mite_populatio(spider_mite.current_population)
            else:
                population_influence[1] = 0
                predator_mite.sudlen_death()

            spider_mite.pass_life_cycle(population_influence[1])
            predator_mite.pass_life_cycle(population_influence[0])

            print("SM:", spider_mite.current_population, spider_mite.relation_management_techniques_id)
            print("PM:", predator_mite.current_population, spider_mite.relation_management_techniques_id)


if __name__ == "__main__":
    main()
