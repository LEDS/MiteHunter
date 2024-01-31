import json
def make_json_file(arq_file, new_data) -> None:
    try:
        found = True
        arq_open =  open(arq_file, 'r+')

        arq_load = json.load(arq_open)
        
        # whit this comented code its impossible add an image twice but the json creation will delay almost 10% more ms time
        #for i in range(len(arq_load)):#change for while
        #    if (new_data['imgOrig']) == (arq_load[i]['imgOrig']):
        #        found = False

        if found:
            arq_load.append(new_data)
            # Salva todos os dados
            with open("Morango.json", "w") as f:
                json.dump(arq_load, f, indent=4)
            arq_open.close()

    except FileNotFoundError:
            file_not_found = []  # Lista vazia para armazenar os dados existentes
            # Se o arquivo não for encontrado, cria um novo arquivo com os dados existentes
            print("Arquivo não encontrado. Criando um novo arquivo com os dados existentes...")
            file_not_found.append(new_data)
            with open(arq_file, 'w') as f:
                json.dump(file_not_found, f, indent=4)
