from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html', {})

def export_data(request):
    if request.method == "POST" and "export_data" in request.POST:
        print("HELLO")
    return render(request, 'export_data_screen/main.html', {})


def exportar_dados(request):
    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )
    cursor = conexao.cursor()

    # Consulta SQL para selecionar os dados que deseja exportar
    consulta_sql = "SELECT * FROM sua_tabela"

    # Executar a consulta
    cursor.execute(consulta_sql)

    # Criar um novo arquivo do Excel
    workbook = Workbook()
    planilha = workbook.active

    # Adicionar cabeçalhos das colunas
    cabecalhos = [i[0] for i in cursor.description]
    planilha.append(cabecalhos)

    # Adicionar os dados
    for linha in cursor:
        planilha.append(linha)

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Salvar o arquivo do Excel em um buffer de memória
    buffer = io.BytesIO()
    workbook.save(buffer)
    buffer.seek(0)

    # Criar uma resposta HTTP com o arquivo do Excel para download
    response = HttpResponse(
        buffer.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=dados_mysql.xlsx'

    return response