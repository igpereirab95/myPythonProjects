# -*- coding: utf-8 -*-

from tabulate import tabulate

# criar funcao para importar em outro arquivo
def modelagemDadosWeb(sitesDic):
    #vai escrever no arquivo
    fileDominios = open('DominioComIp.txt','w')

    for linha in sitesDic:   
        inserirDominios=[] #cria uma nova lista com as informações para ser usado como string posteriormente
        inserirDominios.append(linha) #insere na lista o ip
        listaDominios = sitesDic.get(linha) #pega os valores da chave do dicionario para criar uma lista nova
        for sites in listaDominios:
            inserirDominios.append(sites) # cada site e um novo item na lista nova

        linhaInserir = "" # variavel vazia para ser incrementada
        for infoLista in inserirDominios:       
            linhaInserir += infoLista+";" # adiciona os itens da lista criando uma string pra gravar no arquivo

        linhaInserir = linhaInserir+"\n" # apenas pra quebrar a linha
        fileDominios.write(linhaInserir) # grava no arquivo IP e dominios relacionados ao IP

    fileDominios.close() # fecha arquivo

    return "Inseridos"

def lerIpDominios():
    
    with open('DominioComIp.txt') as f: # le o arquivo e grava a saida em uma lista chamada f
        lines = f.read().splitlines()

    dicNovo = {} #novo dicionário que será usado para mandar pra função tabelarDic
    
    for i in lines: # le a lista e splita a string que vira outra lista que vai popluar o dicionario acima
        i = i.split(';')
        dicNovo[i[0]] = i[1:-1]

    f.close()

    return dicNovo

def tabelarDic(siteDic):

    dicTabulado = {}

    for numDic,i in enumerate(siteDic): # cria um número para e usa o interator para lidar no laço
    
        dicTabulado[i] = siteDic[i] #atribuo ao dicionario os valores

        if numDic % 6 == 0 and numDic > 0: # se for maior que zero e divísil por 6 ele limpa, para criar uma quebra de linha no print
            print("-"*210)
            print(tabulate(dicTabulado,headers="keys", tablefmt="github"))
            print("-"*210)
            dicTabulado.clear() #limpa dicionário

        # print(tabulate(dicTabulado,headers="keys", tablefmt="github"))

    print(tabulate(dicTabulado,headers="keys", tablefmt="github"))    
