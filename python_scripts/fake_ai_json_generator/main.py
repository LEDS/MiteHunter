from Gerador_de_Dados import FakeDataGenerator
from mites import SpiderMite, PredatoryMite, GeneralisPredatoryMite

from random import randint
from json import dump

infestation_level = {
    "very waek": 1,
    "weak": 2,
    "moderated": 3,
    "high": 4,
    "strong": 5,
    "very strong": 6,
    "arachnophobes bware": 7,
    "give up and set fire": 8,
    "they will rule the wolrd": 9,
    "the eleventh plaugue of egypt": 10
}


# Simulate an ambience
def main():
    generate_json_file = False
    generate_mysql_code_file = False
    do_inserts = False
    farmers_number = 10
    plantation_per_farmer = (2, 5)  # Range of minimal and max plantatios a farmer could have 
    experiment_per_plantation = (4, 5)
    samples_per_experimente = (1, 3)
    infestation_level = "moderated"
    start_analisys_time = "2023-01-01"

    next_experiment_id = 10  # put here the last experiment ID plus 1, if it's the first experimente use 1
    next_sample_id = 10  # put here the last sample ID plus 1, if it's the first experimente use 1
    next_plantation_id = 10  # put here the last plantation ID plus 1, if it's the first experimente use 1
    next_farmer_id = 10  # put here the last farmer ID plus 1, if it's the first experimente use 1

    spidermite = SpiderMite()
    predatormite = PredatoryMite()
    generalismite = GeneralisPredatoryMite()

    # Generate Data
    fake_data_generator = FakeDataGenerator()

    farmers_list = fake_data_generator.generate_farmers_brazil(farmers_number)
    plantations = []
    experiments = []

    for farmer_data in range(len(farmers_list)):
        farmer_name = farmers_list[farmer_data][0]
        farmaer_plantation_number = randint(plantation_per_farmer[0], plantation_per_farmer[1])
        farmer_plantation = fake_data_generator.generate_plantations(farmaer_plantation_number)
        
        plantations[farmer_name] = farmer_plantation
        for plantation in farmer_plantation:
            current_time = start_analisys_time
            spidermite.current_population = plantation[1] * infestation_level[infestation_level]

            for exeperiment in range(randint(experiment_per_plantation[0], experiment_per_plantation[1])):
                for sample in range(randint(samples_per_experimente[0], samples_per_experimente[1])):



if __name__ == "__main__":
    main()
