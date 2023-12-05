from faker import Faker
from datetime import date, timedelta
from datetime import datetime
import random
import math
import conexao

def Create_Farmer(qnt):
    '''
    This function recieve the quantity of agricutors when will be genereted and return a dictionary containing the farmers date
    :param qnt: quantitie of farmers waht will be generated
    :return: dictionary whith farmers informations
    '''
    
    fake = Faker('pt_BR')
    farmers = {}

    for c in range(qnt):
        
        cpf   = fake.cpf()
        name  = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        adres = fake.address()
        
        person = [cpf, name, email, phone, adres]
        farmers[c] = person


    return farmers



def Create_Plantation(qnt):
    '''
    This function recieve the quantity of plantantions when will be genereted and return a dictionary containing your date
    :param qnt: quantitie of plantations waht will be generated
    :return: dictionary whith plantations informations
    '''
    
    fake = Faker('pt_BR')
    Plantations = {}
    cultivars_list = ['Cabrillo', 'San Andreas', 'Albion', 'Monterey', 'Portola' , 'Aromas' 'Fronteras' , 'Merced' , 'Camino Real' , 'Camarosa']

    for c in range(qnt):
        name = fake.street_prefix()
        num_plants=random.randint(20, 10000)
        cultivares = cultivars_list[random.randint(0, len(cultivars_list)-1)]
        area = random.randint(10, 10000)
        latitude = fake.latitude()
        longitude = fake.longitude()
    
        plantacao = [name, num_plants, cultivares, area, latitude, longitude]
        Plantations[c] = plantacao    
    return Plantations



def Criar_TipoPlantacao():
    '''
    This function return a list containing the categories of plantations
    '''
    
    l_typePlantation = ['Suspenso', 'Reboleira', 'Canteiros Elevados']
    
    return l_typePlantation



def __cria_l_qnt_mites(amostra_id, qntSamp, taxaEfet, cursor_aux):
    """
    This returns a list with the quantities of mites to be inserted, e.g. [[2], [23, 20, 17], [24, 18, 14]].
    In this list, the first value is the number of mites observed and each list the progression of qnt in each sample
    :amostra_id: id of sample
    :qntSamp: quantitie of samples qhat will be generated
    :taxaEfet: quantitie tax variation of mites in each sample
    :cursor_aux: cursor whith DB connection for querys
    :return: list whith mites quantities for each sample 
    """
    
    l_qnt_mites = []
    
    #select the quantities of each mite in that of the last sample
    query   = 'SELECT qtd, acaro_id, amostra_id FROM Inventario.AmostraAcaro WHERE amostra_id = %s ORDER BY acaro_id '
    cursor_aux.execute(query, [amostra_id])
    
    
    #reading of initial quantities
    result = cursor_aux.fetchall()
    for qnt, _, _ in result:
        l_qnt_mites.append(math.floor(qnt*(1.3)))      #armazena já aplicando a variação padrão
    
        
    #add n samples by applying the rate
    qntMonitored = len(l_qnt_mites)
    for i in range(qntSamp):
        for j in range(qntMonitored):
            
            if j != 2 and j != 3: #verify if id correspond to predador mite
                l_qnt_mites.append(math.floor(l_qnt_mites[i*qntMonitored + j]*(1 + taxaEfet)))   
            else:
                l_qnt_mites.append(l_qnt_mites[i*qntMonitored + j])
    


    #organize in list the quantities what is arranged sequentially
    qnt_mites = []
    for i in range(qntMonitored):
        qnt_mites.append([])

    for i in range (qntSamp+1):
        for j in range(qntMonitored):
            qnt_mites[j].append(l_qnt_mites[qntMonitored*i + j])
 
    
    qnt_mites =  [sublista for sublista in qnt_mites if sublista] #remove listas vazias
            
    return qnt_mites



def insert_Amostra_Taxa(ExperId, date, taxaEfet, qntSamp):  #unused
    '''
    This function receives the experiment id, the effectiveness rate and the number of samples that will be generated,
    generates and executes inserts in the DB
    '''
    
    #DB connection
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    
    #int cursor for querys
    aux = cnn.cursor()
    
    #selects samples ordered descending by date
    query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra ORDER BY data_amostra desc'
    aux.execute(query)
    
    
    #reading the first line to get the ID of the last sample of the experiment
    result = aux.fetchall()
    prev_samp_id, _, _ = result[0]
    
    
    #generating the list with the quantities of mites based on the rate and the last sampling
    l_Qnt = __cria_l_qnt_mites(prev_samp_id, qntSamp, taxaEfet, aux)
    
    #selects samples ordered descending by date
    query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra ORDER BY data_amostra desc'
    aux.execute(query)


def get_date_amostr(experimento_id):
    
    '''s
    This function recieve a experiment_id and return the date of the last sample carried out
    :param experimento_id: id for a especific sequence of samples in a plantation
    :return: a string date. ex:"2023-05-28"
    '''
    
    #DB connection
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    
    #int cursor for querys
    aux = cnn.cursor()
    
    #selects samples ordered descending by date
    query   = 'SELECT experimento_id, data_amostra AS data FROM Inventario.Amostra WHERE experimento_id = %s ORDER BY data_amostra desc'
    aux.execute(query, ([experimento_id]))
    
    
    #reading the first line to get the ID of the last sample of the experiment
    result = aux.fetchall()
    _, date = result[0]
    
    return date


def jsons_generate(l_mites, initialDate, experimento_id):
    
    '''
    This function recieve a list containing the mites quantities in samples, the first date and the experiment_id and 
    return a dictionary simulating the AI output
    :param l_mites: lits with values in each sample
    :param initialDate: date of first sample
    :param experimento_id: id of experiment when samples will be generated
    :return: list of json dictionarys on same format of AI output
    '''
    
    l_jsons = []
    date = initialDate

    #dictionary assembly
    if l_mites:
        for i in range(len(l_mites[0])):
            
            qntAcaros = len(l_mites)
            date = date + timedelta(7)
            json = {}
            
            amostras_acaro = []
            for j in range(qntAcaros):
                amostras_acaro.append(str(l_mites[j][i]))
            
            json["info"]    = [str(date) , str(experimento_id)]
            json["amostra"] = amostras_acaro
            
            l_jsons.append(json)
                    
    return l_jsons
    

def gera_jsons_insert():
    
    '''
    This is the main function, her controll the process from connection in DB to generation json
    '''
    
    lista_jsons = []
    
    for i in range(1, 15):
        experimento_id = i
        
        dateExp = get_date_amostr(experimento_id)        
        
        cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
        aux = cnn.cursor()
        
        #select the samples ordered descending by the date
        query   = 'SELECT id, experimento_id, data_amostra AS data FROM Inventario.Amostra WHERE experimento_id = %s ORDER BY data_amostra desc'
        aux.execute(query, [experimento_id])
        
        
        #reading the first line to get the ID of the last sample of the experiment
        result = aux.fetchall()
        prev_samp_id, _, _ = result[0]
        
        
        randNum = (random.randint(-15, 15)/100)
        l_mites = __cria_l_qnt_mites(prev_samp_id, 20, randNum, aux)
        

        #transforms the values ​​into json
        lista_jsons += jsons_generate(l_mites, dateExp, experimento_id)
        
            
    jsons_insert_query(lista_jsons, dateExp)


def jsons_insert_query(jsonsList, dateExp):
    
    '''
    This function use a json to insert samples in Amostra and output in saida.txt insert querys for AmostraAcaro
    '''
    
    cnn = conexao.bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    aux = cnn.cursor()
    
    for json in jsonsList:
        
        query = "INSERT INTO Inventario.Amostra (Experimento_id, data_amostra) VALUES (%s, %s)"
        
        info = json["info"]
        date = json["amostra"]
        
        aux.execute(query, [info[1], info[0]])
        
        
        #seleciona as amostras ordenadas descrecentemente pela date
        query   = 'SELECT id, experimento_id, data_amostra AS date FROM Inventario.Amostra ORDER BY id desc'
        aux.execute(query)
        
        
        #leitura da primeira linha para pegar id da ultima amostra do experimento
        result = aux.fetchall()
        prev_samp_id, _, _ = result[0]
        
        query = "INSERT INTO Inventario.AmostraAcaro (acaro_id, amostra_id, qtd) VALUES (%s, %s, %s)"
        
        for i in range(1, len(date)):
            print(query, (f"{i}", f"{prev_samp_id}", date[i-1]))
            aux.execute(query, (f"{i}", f"{prev_samp_id}", date[i-1]))  
            
    cnn.commit()
    
if __name__ == '__main__':
    gera_jsons_insert()        
