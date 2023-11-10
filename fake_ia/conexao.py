#   Script de conexão ao Banco de Dados
# 
#   
#   Informações do BD Docker
#
#   172.19.105.24:3306
#   root
#   12345
#

import mysql.connector


def bd_connect(host, nome_bd, login, senha):
    
    connection = mysql.connector.connect(
        host     = host,
        user     = login,
        password = senha,
        database = nome_bd,
    )
    
    return connection


def main():
    
    cnn = bd_connect('172.19.105.24', 'Inventario', 'root', '12345')
    
    #iniciando cursor
    aux = cnn.cursor()
    
    #realizando a query
    query  = 'SELECT * from Agricultor'
    aux.execute(query)
    
    #leitura das rows
    result = aux.fetchall()
    print(result)
    

if __name__ == '__main__':
    main()