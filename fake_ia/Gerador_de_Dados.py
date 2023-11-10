from faker import Faker
import random
import math
import mysql.connector
import conexao
import datetime

def Criar_Agricultor(qnt):
    
    fake = Faker('pt_BR')
    Agricultores = {}

    for c in range(qnt):
        
        cpf   = fake.cpf()
        nome  = fake.name()
        email = fake.email()
        telef = fake.phone_number()
        ender = fake.address()
        
        pessoa = [cpf, nome, email, telef, ender]
        Agricultores[c] = pessoa


    return Agricultores



def Criar_Plantacao(qnt):
    fake = Faker('pt_BR')
    Plantacoes = {}
    lista_cultivares = ['Cabrillo', 'San Andreas', 'Albion', 'Monterey', 'Portola' , 'Aromas' 'Fronteras' , 'Merced' , 'Camino Real' , 'Camarosa']

    for c in range(qnt):
        nome = fake.street_prefix()
        numero_plantas=random.randint(20, 10000)
        cultivares = lista_cultivares[random.randint(0, len(lista_cultivares)-1)]
        area = random.randint(10, 10000)
        latitude = fake.latitude()
        longitude = fake.longitude()
    
        plantacao = [nome, numero_plantas, cultivares, area, latitude, longitude]
        Plantacoes[c] = plantacao    
    return Plantacoes

def Criar_TipoPlantacao(qnt):
    
    lista_TipoPlantacoes = ['Suspenso', 'Reboleira', 'Canteiros Elevados']
    
    return lista_TipoPlantacoes


'''
Essa função recebe ... e retorna uma lista com as quantidades de acaro para ser inseridas ex: [[2], [23, 20, 17], [24, 18, 14]] 
onde nessa lista, o primeiro valor é o nº de acaros observados e cada lista a progressão de qnt em cada amostra
modelo de chamada de função para amostra_id = 1, 20 amostras, taxa de -10% e cursor aberto em aux: lista = __cria_lista_qnt_acaros(["1"], 20, -0.1, aux)
'''
def __cria_lista_qnt_acaros(amostra_id, qntAmos, taxaEfet, cursor_aux):
    
    lista_qnt_acaros = []
    
    #seleciona as as quantidades de cada acaro na da ultima amostra
    query   = 'SELECT qtd, acaro_id, amostra_id FROM Inventario.AmostraAcaro WHERE amostra_id = %s ORDER BY acaro_id '
    cursor_aux.execute(query, amostra_id)
    
    
    #leitura das quantidades iniciais
    result = cursor_aux.fetchall()
    NumAcaroMonit = 0
    for qnt, _, _ in result:
        lista_qnt_acaros.append(math.floor(qnt*(1.3)))      #armazena já aplicando a variação padrão
        NumAcaroMonit += 1
        
    #adiciona n amostras aplicando a taxa
    print(lista_qnt_acaros)
    for i in range(qntAmos):
        #print(f"lista no indice {i*3} = {lista_qnt_acaros[i*3]} * {(1 + taxaEfet)} = {math.floor(lista_qnt_acaros[i*3]*(1 + taxaEfet))}")
        lista_qnt_acaros.append(math.floor(lista_qnt_acaros[i*3]*(1 + taxaEfet)))    
        lista_qnt_acaros.append(math.floor(lista_qnt_acaros[i*3+1]*(1 + taxaEfet)))    
        lista_qnt_acaros.append(math.floor(lista_qnt_acaros[i*3+2]*(1 + taxaEfet)))      
    
    lista_qnt_acaros.insert(0, NumAcaroMonit)   #adiciona a quantidade de acaros sendo monitorados no [0] da lista    


    #organiza em listas as quantidades estão dispostas sequencialmente
    acaros = lista_qnt_acaros[0]
    lista_qnt_acaros.pop(0)
    qnt_Acaros = [[], [], []]

    for i in range (0, 21):
        qnt_Acaros[0].append(lista_qnt_acaros[3*i])
        qnt_Acaros[1].append(lista_qnt_acaros[3*i+1])
        qnt_Acaros[2].append(lista_qnt_acaros[3*i+2]) 
    
    
    return qnt_Acaros


#teste função
cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')

#iniciando cursor para querys
aux = cnn.cursor()

lista_acaros_valores_teste = __cria_lista_qnt_acaros(["1"], 20, -0.1, aux)

print(lista_acaros_valores_teste)

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


'''Essa função recebe o id do experimento, o id da 1ª amostra, n quantidadede de amostras e o cursor da conexão e insere |listaQnt| amostras para o experimento'''
def func_Insert_AmostraAcaro_taxa(experimento_id, amostra_id, listaQnt, cursor):
    
    #busca o ultimo valor amostrado para cada acaro 
    query = 9



'''Essa função recebe o id do experimento, a taxa de efetividade e a quantidade de amostras que serão geradas e gera e executas os inserts no BD'''
def insert_Amostra_Taxa(ExperId, data, taxaEfet, qntAmos):
    
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
    func_Insert_AmostraAcaro_taxa(experimento_id, amostra_id, listaQnt, aux)



#insert_AmostraAcaro_Taxa(2, '2026-07-27', 10, 10)

