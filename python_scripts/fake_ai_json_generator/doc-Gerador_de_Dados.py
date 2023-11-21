from faker import Faker
from datetime import date, timedelta
from datetime import datetime
import random
import math
import conexao




def __cria_lista_qnt_acaros(amostra_id, qntAmos, taxaEfet, cursor_aux):
    
    """
    Essa função recebe ... e retorna uma lista com as quantidades de acaro para ser inseridas ex: [[2], [23, 20, 17], [24, 18, 14]] 
    onde nessa lista, o primeiro valor é o nº de acaros observados e cada lista a progressão de qnt em cada amostra
    modelo de chamada de função para amostra_id = 1, 20 amostras, taxa de -10% e cursor aberto em aux: lista = __cria_lista_qnt_acaros(["1"], 20, -0.1, aux)
    """
    
    lista_qnt_acaros = []
    
    #seleciona as as quantidades de cada acaro na da ultima amostra
    query   = 'SELECT qtd, acaro_id, amostra_id FROM Inventario.AmostraAcaro WHERE amostra_id = %s ORDER BY acaro_id '
    cursor_aux.execute(query, [amostra_id])
    
    
    #leitura das quantidades iniciais
    result = cursor_aux.fetchall()
    for qnt, _, _ in result:
        lista_qnt_acaros.append(math.floor(qnt*(1.3)))      #armazena já aplicando a variação padrão
    
        
    #adiciona n amostras aplicando a taxa
    qntMonitorados = len(lista_qnt_acaros)
    for i in range(qntAmos):
        #print(f"lista no indice {i*3} = {lista_qnt_acaros[i*3]} * {(1 + taxaEfet)} = {math.floor(lista_qnt_acaros[i*3]*(1 + taxaEfet))}")
        for j in range(qntMonitorados):
            
            if j != 2 and j != 3: #verify if id correspond to predador mite
                lista_qnt_acaros.append(math.floor(lista_qnt_acaros[i*qntMonitorados + j]*(1 + taxaEfet)))   
            else:
                lista_qnt_acaros.append(lista_qnt_acaros[i*qntMonitorados + j])
    


    #organiza em listas as quantidades estão dispostas sequencialmente
    qnt_Acaros = []
    for i in range(qntMonitorados):
        qnt_Acaros.append([])

    for i in range (qntAmos+1):
        for j in range(qntMonitorados):
            qnt_Acaros[j].append(lista_qnt_acaros[qntMonitorados*i + j])
 
    
    qnt_Acaros =  [sublista for sublista in qnt_Acaros if sublista] #remove listas vazias
            
    return qnt_Acaros

'''
#teste função
cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')

#iniciando cursor para querys
aux = cnn.cursor()

lista_acaros_valores_teste = __cria_lista_qnt_acaros(["1"], 20, -0.05, aux)

print(lista_acaros_valores_teste) '''

'''acaros = lista_acaros_valores_teste[0]
lista_acaros_valores_teste.pop(0)
texto = [str(), str(), str()]
print("itens na lista:", len(lista_acaros_valores_teste), "quant acaros:", acaros)

for i in range (0, 21):
    texto[0] += f" {lista_acaros_valores_teste[3*i]},"
    texto[1] += f" {lista_acaros_valores_teste[3*i+1]},"
    texto[2] += f" {lista_acaros_valores_teste[3*i+2]},"

for c in range(3):
    print(texto[c])
'''

def insert_Amostra_Taxa(ExperId, data, taxaEfet, qntAmos):
    '''Essa função recebe o id do experimento, a taxa de efetividade e a quantidade de amostras que serão geradas e gera e executas os inserts no BD'''
    
    #conexão ao BD
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    
    #iniciando cursor para querys
    aux = cnn.cursor()
    
    #seleciona as amostras ordenadas descrecentemente pela data
    query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra ORDER BY data_amostra desc'
    aux.execute(query)
    
    
    #leitura da primeira linha para pegar id da ultima amostra do experimento
    result = aux.fetchall()
    amostra_id_anterior, _, _ = result[0]
    
    
    #gerando a lista com as quantidades de acaros baseado na taxa e na ultima amostragem
    listaQnt = __cria_lista_qnt_acaros(amostra_id_anterior, qntAmos, taxaEfet, aux)
    
    
    '''
    #realiza o insert da primeira amostra
    query   = 'INSERT INTO Inventario.Amostra (experimento_id, data_amostra) VALUES (%s, %s)'
    values = (ExperId, data)
    aux.execute(query, values)
    '''
    
    #seleciona as amostras ordenadas descrecentemente pela data
    query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra ORDER BY data_amostra desc'
    aux.execute(query)
    
    
    #leitura da primeira linha
    result = aux.fetchall()
    amostra_id, experimento_id, data_amostra = result[0]
    #print(f"O id da amostra é {id}, o o id do experimento é {experimento_id} e essa contagem ocorreu em {data_amostra}")
    
    
    #realizando os inseerts em Amostra_Acaro
    #func_Insert_AmostraAcaro_taxa(experimento_id, amostra_id, listaQnt, aux)


def get_data_amostr(experimento_id):
    
    #conexão ao BD
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    
    #iniciando cursor para querys
    
    aux = cnn.cursor()
    
    #seleciona as amostras ordenadas descrecentemente pela data
    query   = 'SELECT experimento_id, data_amostra AS data FROM Inventario.Amostra WHERE experimento_id = %s ORDER BY data_amostra desc'
    aux.execute(query, ([experimento_id]))
    
    
    #leitura da primeira linha para pegar id da ultima amostra do experimento
    result = aux.fetchall()
    _, data = result[0]
    
    cnn.rollback()
    
    return data


def gera_jsons(listaAcaros, dataInicial, experimento_id):
    
    l_jsons = []
    data = dataInicial

    #montagem do dicionario
    if listaAcaros:
        for i in range(len(listaAcaros[0])):
            
            qntAcaros = len(listaAcaros)
            data = data + timedelta(7)
            json = {}
            
            amostras_acaro = []
            for j in range(qntAcaros):
                amostras_acaro.append(str(listaAcaros[j][i]))
            
            json["info"]    = [str(data) , str(experimento_id)]
            json["amostra"] = amostras_acaro
            
            l_jsons.append(json)
        
    
    #print(l_jsons)
        
    return l_jsons    


# Main Function
def gera_jsons_insert():
    lista_jsons = []
    
    for id in range(1, 15):  # Arbitrary Valeus for Experiment ID
        experimento_id = id
        
        dataExp = get_data_amostr(experimento_id)        
        
        cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
        aux = cnn.cursor()
        
        #seleciona as amostras ordenadas descrecentemente pela data
        query   = 'SELECT id FROM Inventario.Amostra WHERE experimento_id = %s ORDER BY id desc'
        aux.execute(query, [experimento_id])
        
        
        #leitura da primeira linha para pegar id da ultima amostra do experimento
        result = aux.fetchall()
        amostra_id_anterior = result[0][0]
        
        
        aleat = (random.randint(-15, 15)/100)
        listaAcaros = __cria_lista_qnt_acaros(amostra_id_anterior, 20, aleat, aux)
        

        #transforma os valores em json
        lista_jsons += gera_jsons(listaAcaros, dataExp, experimento_id)
        
            
    jsons_insert_query(lista_jsons, dataExp)


def jsons_insert_query(jsonsList, dataExp):
    
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    aux = cnn.cursor()
    
    with open('saida.txt', 'w') as arquivo:
        for json in jsonsList:
            
            query = "INSERT INTO Inventario.Amostra (Experimento_id, data_amostra) VALUES (%s, %s)"
            
            info = json["info"]
            data = json["amostra"]
            
            aux.execute(query, [info[1], info[0]])
            
            
            #seleciona as amostras ordenadas descrecentemente pela data
            query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra ORDER BY id desc'
            aux.execute(query)
            
            
            #leitura da primeira linha para pegar id da ultima amostra do experimento
            result = aux.fetchall()
            print(result[0])
            amostra_id_anterior, _, _ = result[0]
            print(amostra_id_anterior)
            
            query = "INSERT INTO Inventario.AmostraAcaro (acaro_id, amostra_id, qtd) VALUES (%s, %s, %s)"
            
            for i in range(1, len(data)+1):
                texto = f"INSERT INTO Inventario.AmostraAcaro (acaro_id, amostra_id, qtd) VALUES ({i}, {amostra_id_anterior}, {data[i-1]})"
                #print(texto)
                arquivo.write(texto)
                
                arquivo.write(";\n")
        cnn.rollback()
    

    
if __name__ == '__main__':
    gera_jsons_insert()        
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    cnn.rollback()
    # print("\n", (__cria_lista_qnt_acaros.__doc__))
    