# -*- coding: utf-8 -*-
# import pegaServer as Ps #cria um alias para o nome do modulo/arquivo usado
# import fileIO as Fio
from classeSites import Sites
# import aux1 as Auxiliar
# import aux2 as Aux2

menuOptions = input('''

    1 - ler arquivo
    2 - imprimir novo arquivo
    3 - Exibir arquivo atual
    4 - sair

''')

site = Sites()

def selecionadaOpcao(menuOpt):
    
    if menuOpt == '1':
        # Auxiliar.imprimeDic(Aux2.criaDicSites())
        site.populaDicionario()
        

    if menuOpt == '2':
        site.modelagemDadosWeb(site.populaDicionario())
        print(site.lerIpDominios())

    if menuOpt == '3':       
        site.tabelarDic(site.lerIpDominios())
        # Fio.tabelarDic(Ps.populaDicionario())

selecionadaOpcao(menuOptions)
