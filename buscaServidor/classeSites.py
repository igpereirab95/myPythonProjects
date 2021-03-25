# -*- coding: utf-8 -*-
from itertools import chain #concatenar listas no for, será usado mais adiante
import subprocess #executa o comando dig para buscar o IP
from tabulate import tabulate #importa classe para criar tabela bonitinha

class Sites:
    #constrói um ojeto vazio
    def __init__(self):        
        self.dicSites = dict()

    #print só pra ver o atributo
    def funcTeste(self):
        print("Testando este objeto",self.get_dicSites())
    
    #seta o atributo com um dicionário
    # def set_dicSites(self, dicSites):
        # self.dicSites = dict()

    def get_dicSites(self):
        return self.dicSites

    def populaDicionario(self):
        
        #abre e le o arquivo 
        lDominio = open('listaDominios.txt','r')
        #executa o comando, deve ser em lista
        comandoShell= ['dig','+short','a','@8.8.8.8']
        #cria a lista com as linhas do arquivo
        lines = lDominio.readlines()
        #fecha o arquivo, pois  nao precisa mais
        lDominio.close()


        #lendo a lista
        for i in lines:    

            #evita excluir na primeira execução pois excluiria o dns do comando
            if lines.index(i) != 0:
                #remove o dominio após a primeira insercao
                comandoShell.pop()

            #aqui tira a quebra de linha \n que tem no arquivo e adiciona o dominio no comando
            comandoShell.append(i.strip())
            
            #aqui vai pegar o IP do dominio
            ipDominio = subprocess.check_output(comandoShell, universal_newlines=True)
            
            self.novoItemDic(ipDominio,i)
        
        return self.get_dicSites()
    
        #funcao que cria o docionario conforme os dominios
    def novoItemDic(self, ip, dominio):
        ip= ip.strip()
        dominio = dominio.strip()
        try:
            self.dicSites[ip].append(dominio)
        except:
            self.dicSites[ip] = [dominio]



    # criar funcao para importar em outro arquivo
    def modelagemDadosWeb(self, sitesDic):
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

    def lerIpDominios(self):
        
        with open('DominioComIp.txt') as f: # le o arquivo e grava a saida em uma lista chamada f
            lines = f.read().splitlines()

        dicNovo = {} #novo dicionário que será usado para mandar pra função tabelarDic
        
        for i in lines: # le a lista e splita a string que vira outra lista que vai popluar o dicionario acima
            i = i.split(';')
            dicNovo[i[0]] = i[1:-1]

        f.close()

        return dicNovo

    def tabelarDic(self, siteDic):

        dicTabulado = {}

        for numDic,i in enumerate(siteDic): # cria um número para usar o interator para lidar no laço
        
            dicTabulado[i] = siteDic[i] #atribuo ao dicionario os valores

            if numDic % 6 == 0 and numDic > 0: # se for maior que zero e divísil por 6 ele limpa, para criar uma quebra de linha no print
                print("-"*210)
                print(tabulate(dicTabulado,headers="keys", tablefmt="github"))
                print("-"*210)
                dicTabulado.clear() #limpa dicionário

            # print(tabulate(dicTabulado,headers="keys", tablefmt="github"))

        print(tabulate(dicTabulado,headers="keys", tablefmt="github"))    
