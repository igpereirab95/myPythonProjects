# -*- coding: utf-8 -*-
# from tabulate import tabulate
# import fileIO as Fio

from classeSites import Sites

sitesDic= {'187.1.132.155': ['lojafisicanaweb.com', 'ljdemo.uni5.net', 'emclojaweb397.uni5.net'], '187.1.132.46': ['emcrestaurante.uni5.net', 'lojawebhmlint.uni5.net'], '187.1.132.116': ['emcdelivery.uni5.net', 'lojafisicanaweb.com.br'], '187.1.132.75': ['emclojaweb345.uni5.net'], '187.1.132.79': ['websotoresoluction.com.br'], '187.1.142.50': ['emclojaweb351.uni5.net'], '187.1.132.86': ['emclojaweb353.uni5.net'], '187.1.142.48': ['emclojaweb398.uni5.net', 'emcb2b.uni5.net'], '187.1.132.83': ['lojawebfacil.com.br', 'emclojaweb457.uni5.net'], '187.1.142.20': ['emclojaweb587.uni5.net']}

dominio = input("dado para criar classe \n -> ")


psites = Sites()

psites.setaDominio(dominio)
psites.set_dicSites(sitesDic)
psites.funcTeste()


# dicTabulado = {}

# for numDic,i in enumerate(sitesDic):
   
#     dicTabulado[i] = sitesDic[i] #atribuo ao dicionario os valores

#     if numDic % 6 == 0 and numDic > 0: # se for maior que zero e divísil por 6 ele limpa, para criar uma quebra de linha no print
#         print("-"*210)
#         print(tabulate(dicTabulado,headers="keys", tablefmt="github"))
#         print("-"*210)
#         dicTabulado.clear() #limpa dicionário

#     # print(tabulate(dicTabulado,headers="keys", tablefmt="github"))

# print(tabulate(dicTabulado,headers="keys", tablefmt="github"))


# print(Fio.lerIpDominios())

# with open('DominioComIp.txt') as f:
#   lines = f.read().splitlines()

# dicNovo = {}
# for i in lines:
#     i = i.split(';')
#     dicNovo[i[0]] = i[1:-1]

# print(dicNovo)
    
    

