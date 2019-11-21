#Senha para poder se cadastrar como gerente = 777
#Só gerente pode cadastrar alguém com permissão de gerente ou se possuir a senha
#Ele ordena os elementos por ordem númerica

from funcao import *
continuar=True
objetivo=""
while objetivo=="":
    objetivo = input("1 - Você deseja se cadastrar, 2- Você já possui uma conta")
    if objetivo =='1':
        criou=cadastrar()
        log(criou,"Se cadastrou")
        print("Logue na sua conta")
        tempo(1)
        armazenarlogin=validarPerm()
        permissao=armazenarlogin[0]
        if permissao=="1" or permissao=="2":
            log(armazenarlogin[1],"Logou")
            print("Você logou")
            tempo(1)
        else:
            print("Login inválido")
            log(armazenarlogin[1],"Login inválido")
            tempo(1)
    elif objetivo=='2':
        armazenarlogin= validarPerm()
        permissao=armazenarlogin[0]
        if permissao=="1" or permissao=="2":
            log(armazenarlogin[1],"Logou")
            print("Você logou")
            tempo(1)
        else:
            print("Login inválido")
            log(armazenarlogin[1],"Login inválido")
            tempo(1)
    else:
        objetivo=""




while permissao=='errou':
    if permissao=='errou':
        perg=input("Deseja logar novamente?(S/N)").upper()
        if perg == 'S':
            armazenarlogin=validarPerm()
            permissao=armazenarlogin[0]
            if permissao=="1" or permissao=="2":
                log(armazenarlogin[1],"Logou")
                print("Você logou")
                tempo(1)
            else:
                print("Login inválido")
                log(armazenarlogin[1],"Login inválido")
                tempo(1)
        elif perg =='N':
            print("Você Saiu do programa")
            log(armazenarlogin[1],"Saiu do programa")
            permissao="sair"
            continuar=False
    



while continuar==True:  
    while permissao == '1':
        opcao= input("O que deseja fazer:\n 1- Cadastrar Login\n 2-Cadastrar Produtos\n 3-Pesquisar produto\n 4- Remover Produto\n 5-Atualizar quantidade do produto\n 6-Ordenar produtos por nome\n 7-Gerar relatório\n 8-Ler log\n 9- Logout\n 0-Sair do programa")
        if opcao =="1":
            cadastrarComoGerente()
            log(armazenarlogin[1],"Cadastrou usuario")
            opcao= "none"
            print("Usuário cadastrado com sucesso")
            tempo(1)
        elif opcao=="2":
            cadastroProduto()
            log(armazenarlogin[1],"Cadastrou produto")
            print("Produto cadastrado com sucesso")
            tempo(1)
        elif opcao=="3":
            nota=input("Digite a nota fiscal que quer procurar:")
            pPesquisado=pesquisarProdutos(nota)
            if pPesquisado=="Nao encontrado":
                print("Produto não está no estoque")
                log(armazenarlogin[1],"Pesquisou produto")
                tempo(1)
            else:
                printarPesquisaOrganizada(pPesquisado)
                log(armazenarlogin[1],"Pesquisou produto")
                tempo(4)
        elif opcao=="4":
            nota2=input("Digite a nota fiscal do produto que quer remover:")
            temRemover=pesquisarProdutos(nota2)
            if temRemover=="Nao encontrado":
                print("Produto não está no estoque")
                log(armazenarlogin[1],"Produto não encontrado para remoção")
                tempo(1)
            else:
                remover(nota2)
                log(armazenarlogin[1],"Removeu produto")
                print("Produto removido com sucesso")
                tempo(1)
        elif opcao=="5":
            nota3=input("Digite a nota fiscal que deseja alterar:")
            temAtt=pesquisarProdutos(nota3)
            if temAtt=="Nao encontrado":
                print("Produto não está no estoque")
                log(armazenarlogin[1],"Produto não encontrado para Atualização")
                tempo(1)
            else:
                atualizar(nota3)
                log(armazenarlogin[1],"Atualizou produto")
                print("Produto atualizado com sucesso")
                tempo(1)
        elif opcao=="6":
            organizar()
            log(armazenarlogin[1],"Ordenou produtos")
            print("Produtos foram ordenados")
            tempo(1)
        elif opcao=="7":
            relatorio()
            log(armazenarlogin[1],"Gerou relatorio")
            print("Relatório gerado")
            tempo(1)
        elif opcao=="8":
            log(armazenarlogin[1],"Leu log")
            lerlog()
        elif opcao=="9":
            log(armazenarlogin[1],"Deslogou")
            print("Você deslogou")
            pergunta=input("Você deseja logar novamente? (S/N)").upper()
            if pergunta=="S":
                armazenarlogin=validarPerm()
                permissao=armazenarlogin[0]
                if permissao=="1" or permissao=="2":    
                    log(armazenarlogin[1],"Logou")
                    print("Você logou")
                    tempo(1)
            elif pergunta=="N":
                log(armazenarlogin[1],"Saiu do programa")
                print("Você saiu do programa")
                permissao=False
                continuar=False
                
        elif opcao=="0":
            log(armazenarlogin[1],"Saiu do programa")
            print("Você saiu do programa")
            permissao=False
            continuar=False

   
   
    while permissao == '2':
        opcao= input("O que deseja fazer:\n 1- Cadastrar Login\n 2-Pesquisar produto\n 9-Logout\n 0- Sair do programa")
        if opcao =="1":
            cadastrar()
            opcao= ""
            log(armazenarlogin[1],"Cadastrou")
            print("Usuário cadastrado com sucesso")
            tempo(1)
        elif opcao=="2":
            nota=input("Digite a nota fiscal que quer procurar:")
            pPesquisado=pesquisarProdutos(nota)
            if pPesquisado=="Nao encontrado":
                print("Produto não está no estoque")
                log(armazenarlogin[1],"Pesquisou produto")
                tempo(1)
            else:
                printarPesquisaOrganizada(pPesquisado)
                tempo(4)
                log(armazenarlogin[1],"Pesquisou produto")
        elif opcao=="9":
            log(armazenarlogin[1],"Deslogou")
            print("Você deslogou")
            pergunta=input("Você deseja logar novamente? (S/N)").upper()
            if pergunta=="S":
                armazenarlogin=validarPerm()
                permissao=armazenarlogin[0]
                if permissao=="1" or permissao=="2":
                    log(armazenarlogin[1],"Logou")
                    print("Você logou")
                    tempo(1)
            elif pergunta=="N":
                log(armazenarlogin[1],"Saiu do programa")
                print("Você saiu do programa")
                permissao=False
                continuar=False
        elif opcao=="0":
            log(armazenarlogin[1],"Saiu do programa")
            print("Você saiu do programa")
            permissao=False
            continuar=False
