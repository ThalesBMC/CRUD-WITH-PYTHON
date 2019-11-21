import time
def tempo(tempoEspera):
    """Demora para o programa rodar"""
    time.sleep(tempoEspera)  
def cadastrar():
    """Faz o cadastro de usuário"""
    login= input('Digite seu login  que quer cadastrar ')
    senha= input('Digite sua senha que quer cadastrar')
    cpf= input('Digite seu cpf que quer cadastrar')
    cadastrarperm = input("Se você tiver senha para escolher sua permissão digite ela, se não digite qualquer coisa para receber a permissão de estagiário")
    if cadastrarperm == '777':
        perme= input("Digite sua permissao 1-Gerente 2-Estagiário :")
    else:
        perme= "2"
    arquivo= open("listadelogins.txt", "a")
    arquivo.write (cpf)
    arquivo.write("\n")
    arquivo.write (login)
    arquivo.write("\n")
    arquivo.write (senha)
    arquivo.write("\n")
    arquivo.write(perme)
    arquivo.write("\n")
    arquivo.close()
    

    return(login)
def cadastrarComoGerente():
    """Faz o cadastro com permissão de gerente"""
    login= input('Digite seu login  que quer cadastrar:')
    senha= input('Digite sua senha que quer cadastrar')
    cpf= input('Digite seu cpf que quer cadastrar:')
    perme= input("Digite sua permissao 1- Gerente ou 2- Estagiário :")
    arquivo= open("listadelogins.txt", "a")
    arquivo.write (cpf)
    arquivo.write("\n")
    arquivo.write (login)
    arquivo.write("\n")
    arquivo.write (senha)
    arquivo.write("\n")
    arquivo.write(perme)
    arquivo.write("\n")
    arquivo.close()

    return()
      
def TirarBarraN(conteudo):
    """Tira o \n da string"""
    palavra=""
    for j in conteudo:
        if j != "\n":
            palavra += j
    return palavra


def leitura():
    """Ler o arquivo e retorna em dicionário"""
    dicLogins={}
    contador=0
    arq=open("listadelogins.txt","r")
    quantidade = arq.readlines()
    arq.close()
    while( contador < len(quantidade) // 4):
        cpf = TirarBarraN(quantidade[4*contador])
        nome = TirarBarraN(quantidade[4*contador+1])
        senha = TirarBarraN(quantidade[4*contador+2])
        perme = TirarBarraN(quantidade[4*contador+3])
        tupla = (nome,senha,perme)
        dicLogins[cpf]=tupla
        contador+=1
    return(dicLogins)

def hora():
    """A data e hora atual"""
    from datetime import datetime
    horario = datetime.now()
    horario = horario.strftime("%d/%m/%Y %H:%M")
    return horario


def validarPerm():
    """Valida se o login e senha estão corretos"""
    login=input("Digite seu login:")
    senha= input("Digite sua senha:")
    perme1= '1'
    perme2='2'
    autorizacao="errou"
    salvarLogin="não tem"
    contas=leitura()
    usuario=contas.keys()
    for chave in usuario:
        if contas[chave] == (login,senha,perme1):
            autorizacao="1"
            salvarLogin=login
        elif contas[chave] == (login,senha,perme2):
            autorizacao="2"
            salvarLogin=login
            
    return (autorizacao,salvarLogin)
        
def cadastroProduto():
    """Cadastra produto"""
    notaFiscal=input("Digite a nota fiscal:")
    nomeProduto=input("Digite o nome do produto:")
    quantidadeProduto=input("Digite a quantidade do produto:")

    horaCri= hora()
    horaAtt= hora()
    criptografar(notaFiscal)
    criptografar(nomeProduto)
    criptografar(quantidadeProduto)
    criptografar(horaCri)
    criptografar(horaAtt)

    return()
def criptografar(elemento):
    """Criptografa produto"""
    chave=open("chavePublica.txt","r")
    quantidade=chave.readlines()
    e=int(TirarBarraN(quantidade[0]))
    n=int(TirarBarraN(quantidade[1]))
    chave.close()
    for j in elemento:
        parte1= ord(j)
        parte2= parte1**e % n
        produtos=open("elementos.txt","a")
        produtos.write(str(parte2))
        produtos.write(" ")
        produtos.close()
    produtos2=open("elementos.txt","a")
    produtos2.write("\n")
    produtos2.close()   
    
    return()
def descriptografar(elemento):
    """Descriptografa"""
    chave=open("chavePrivada.txt","r")
    quantidade=chave.readlines()
    d=int(TirarBarraN(quantidade[0]))
    n=int(TirarBarraN(quantidade[1]))
    chave.close()
    palavrafinal=""
    cont=0
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    pteste=""
    for m in elemento:
        if m == " ":
            strj = int(pteste)
            descript = strj**d % n
            palavrafinal+= chr(descript)
            cont+=1
            pteste=""
        else:
            pteste+=str(m)            
        
    
   
    return(palavrafinal)


def produtos():
    """Dicionário com produtos"""
    dicProdutos={}
    contador=0
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    qtprodutos= len(quantidade) // 5
    while( contador < qtprodutos):
        notaFiscal = descriptografar(TirarBarraN(quantidade[5*contador]))
        nomeProduto = descriptografar(TirarBarraN(quantidade[5*contador+1]))
        quant= descriptografar(TirarBarraN(quantidade[5*contador+2]))
        horaCri = descriptografar(TirarBarraN(quantidade[5*contador+3]))
        horaAtt = descriptografar(TirarBarraN(quantidade[5*contador+4]))
        tupla=(nomeProduto,quant,horaCri,horaAtt)
        dicProdutos[notaFiscal]=tupla
        contador+=1
    
        
    return(dicProdutos)

    
def pesquisarProdutos(nota):
    """Pesquisa se o produto está ou não no dicionário"""
    contas=produtos()
    usuario=contas.keys()
    for chave in usuario:
        if chave == nota :
            return(contas[chave])

    return("Nao encontrado")



def remover(nota):
    """Remove produto do arquivo"""
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    qtprodutos= (len(quantidade) // 5)
    cont=0
    arq=open("elementos.txt","w")
    arq.close()
    while cont < (qtprodutos ) :
        notaFiscal = str(descriptografar(TirarBarraN(quantidade[5*cont])))
        nomeProduto = str(descriptografar(TirarBarraN(quantidade[5*cont+1])))
        quant= str(descriptografar(TirarBarraN(quantidade[5*cont+2])))
        horaCri = str(descriptografar(TirarBarraN(quantidade[5*cont+3])))
        horaAtt = str(descriptografar(TirarBarraN(quantidade[5*cont+4])))
        cont+=1
        if notaFiscal != nota:
            criptografar(notaFiscal)
            criptografar(nomeProduto)
            criptografar(quant)
            criptografar(horaCri)
            criptografar(horaAtt)
            
            
    return()
 
def atualizar(nota):
    """Atualiza produto do arquivo"""
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    qtprodutos= (len(quantidade) // 5)
    trocar=input("Digite o valor que deseja substituir:")
    cont=0
    arq=open("elementos.txt","w")
    arq.close()
    horaNova=hora()
    while cont < qtprodutos :
        notaFiscal = descriptografar(TirarBarraN(quantidade[5*cont]))
        nomeProduto = descriptografar(TirarBarraN(quantidade[5*cont+1]))
        quant= descriptografar(TirarBarraN(quantidade[5*cont+2]))
        horaCri = descriptografar(TirarBarraN(quantidade[5*cont+3]))
        horaAtt =descriptografar(TirarBarraN(quantidade[5*cont+4]))
        cont+=1
        if notaFiscal != nota:
            criptografar(notaFiscal)
            criptografar(nomeProduto)
            criptografar(quant)
            criptografar(horaCri)
            criptografar(horaAtt)
        else:
            colocar=open("elementos.txt","a")
            criptografar(notaFiscal)
            criptografar(nomeProduto)
            criptografar(trocar)
            criptografar(horaCri)
            criptografar(horaNova)
            colocar.close()
               
    return()



def organizar():
    """Organiza por ordem alfabética os elementos"""
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    qtprodutos= (len(quantidade) // 5)
    cont=0
    contador=0
    cont2=0
    lista=[]
    lista2=[]
    while cont < qtprodutos  :
        nomeProduto = descriptografar(TirarBarraN(quantidade[5*cont+1]))
        cont+=1
        lista.append(nomeProduto)
    while contador<qtprodutos:
        lista2.append(min(lista))
        lista.remove(min(lista))
        contador+=1
    arq2=open("elementos.txt","w")
    arq2.close()
    while cont2 < qtprodutos   :
        if len(lista2)==0:
            return()
        notaFiscal = str(descriptografar(TirarBarraN(quantidade[5*cont2])))
        nomeProduto= str(descriptografar(TirarBarraN(quantidade[5*cont2+1])))
        quant= str(descriptografar(TirarBarraN(quantidade[5*cont2+2])))
        horaCri =str(descriptografar(TirarBarraN(quantidade[5*cont2+3])))
        horaAtt = str(descriptografar(TirarBarraN(quantidade[5*cont2+4])))
        if lista2[0]== nomeProduto: 
            criptografar(notaFiscal)
            criptografar(nomeProduto)
            criptografar(quant)
            criptografar(horaCri)
            criptografar(horaAtt)
            lista2.remove(lista2[0])
            cont2=0
        else:
            cont2+=1
    
    return()


def relatorio():
    """Gera um relatório com os elementos"""
    arq=open("elementos.txt","r")
    quantidade = arq.readlines()
    arq.close()
    qtprodutos= (len(quantidade) // 5)
    cont=0
    f=open('relatorio.csv','w')
    f.write("NOTA FISCAL;")
    f.write("NOME DO PRODUTO;")
    f.write("QUANTIDADE;")
    f.write("CRIACAO;")
    f.write("ULTIMA ATUALIZACAO;")
    f.write("\n")
    f.close()
    while cont < qtprodutos :
        notaFiscal = str(descriptografar(TirarBarraN(quantidade[5*cont])))
        notaFiscal+="."
        notaFiscal+= ";"
        nomeProduto = str(descriptografar(TirarBarraN(quantidade[5*cont+1])))
        nomeProduto+="."
        nomeProduto+=";"
        quant= str(descriptografar(TirarBarraN(quantidade[5*cont+2])))
        quant +="."
        quant +=";"
        horaCri = str(descriptografar(TirarBarraN(quantidade[5*cont+3])))
        horaCri+="."
        horaCri+=";"
        horaAtt = str(descriptografar(TirarBarraN(quantidade[5*cont+4])))
        horaAtt+="."
        horaAtt+=";"
        cont+=1
        b= open('relatorio.csv','a')
        b.write(notaFiscal)
        b.write(nomeProduto)
        b.write(quant)
        b.write(horaCri)
        b.write(horaAtt)
        b.write("\n")
        b.close()
    return()

def log(nome,oque):
    """Faz o log """
    nome2=nome
    quando=hora()
    oque2=oque
    arqui=open("log.txt","a")
    arqui.write(nome2)
    arqui.write("\n")
    arqui.write(quando)
    arqui.write("\n")
    arqui.write(oque2)
    arqui.write("\n")
    arqui.close()

    return()
def lerlog():
    """Faz a leitura do log e printa no programa"""
    arq3=open("log.txt","r")
    quantidade3 = arq3.readlines()
    arq3.close()
    qtprodutos3= (len(quantidade3) // 3)
    cont3=0
    while cont3 < qtprodutos3 :
        nome = TirarBarraN(quantidade3[3*cont3])
        nome+="."
        quando = TirarBarraN(quantidade3[3*cont3+1])
        quando+="."
        oque= TirarBarraN(quantidade3[3*cont3+2])
        oque+="."
        cont3+=1
        print(("Quem realizou a atividade:"+nome,"Quando foi realizada:"+quando,"O que foi realizado:"+oque))
    return()
def printarPesquisaOrganizada(pPesquisado):
    """Para poder organizar os dados do dicionário para printar"""
    listaPesquisado=(pPesquisado)
    nomePesquisado=" Nome do produto: "
    nomePesquisado+=listaPesquisado[0]
    nomePesquisado+="\n"
    quantidadePesquisada="Quantidade: "
    quantidadePesquisada+=listaPesquisado[1]
    quantidadePesquisada+="\n"
    criacaoPesquisada="Hora de criaçao: "
    criacaoPesquisada+=listaPesquisado[2]
    criacaoPesquisada+="\n"
    attPesquisada="Hora de atualizaçao: "
    attPesquisada+=listaPesquisado[3]
    attPesquisada+="\n"
    print(nomePesquisado,quantidadePesquisada,criacaoPesquisada,attPesquisada)
    
