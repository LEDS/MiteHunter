def main():
    jsonData = [
    {
        'foliolo':
            {'imgOrig': 'img',
            'imgProc': 'imgP',
            'rajado': 10, 
            'macropilis': 5, 
            'californicus': 2},
            'cultivo_id': 13, 
            'data_Amos': '2023-10-25'
    }]

    dictP = {'fidelis@gmail.com_13_03042024_145758': {'with_predator_with_mite_percentage': 0.5, 'with_predator_without_mite_percentage': 0.5, 'final_class': 'with_predator_with_mite', 'suggested_action': 'Não fazer nada!'}, 'wilsiman.evangelista.ifes@gmail.com_10_20240129_125740': {'one_to_five_mite_percentage': 0.5, 'with_predator_with_mite_percentage': 0.5, 'final_class': 'one_to_five_mite', 'suggested_action': 'Jogar água!'}}

    for file_name, counts in dictP.items():
        for key, value in counts.items():
            jsonData[-1][key] = value
    print(jsonData)
if __name__ == "__main__":
    main()