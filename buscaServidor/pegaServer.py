import subprocess

ipWebDominio={}

#funcao que cria o docionario conforme os dominios
def novoItemDic(ip,dominio):
    ip= ip.strip()
    dominio = dominio.strip()
    try:
        ipWebDominio[ip].append(dominio)
    except:
        ipWebDominio[ip] = [dominio]


def populaDicionario():
    
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
        
        novoItemDic(ipDominio,i)

        # print("Domínio {} ....... IP ->> {}".format(i.strip(), ipDominio))
    
    return ipWebDominio
