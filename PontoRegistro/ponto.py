from flask import Flask, url_for
from markupsafe import escape
import datetime,pytz,os

app = Flask(__name__)

# @app.route('/')
# def gravar_arquivo():

#     return "gravado horário"

def gravando_horarios(username,acao):
    # armazena o horário
    pontoRegistro=datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
    
    #criar string a ser inserida
    gravarPonto=pontoRegistro.strftime("%c")+" - "+acao+" \n"

    #cria arquivo conforme o nome
    criaNomeArquivo="./registropontos/registro-ponto-"+username+".txt"

    #cria arquivo se não tiver usando o nome o a é para append, ou seja adicionar ao final numa nova linha
    arquivoRegistros=open(criaNomeArquivo,"a")

    #criar condicao de quabra de linhas por dia, pra nao ficar amontoado 
    if acao == "entrada":
        arquivoRegistros.write('\n')

    #escreve a informação
    arquivoRegistros.write(gravarPonto)

    #fecha arquivo
    arquivoRegistros.close()

@app.route('/')
def index():
    return 'vai ter botões aqui'

#rota que pega o nome do usuário e a ação que pretende fazer, inicialmente pegar pela url porteriormente pelo botão, obrigatoriamente mandar user e ação
@app.route('/user/<username>/<acao>')
def profile(username,acao):
    #retorno tem que ser único
    gravando_horarios(username,acao)
    return "Gravado"


