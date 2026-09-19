import json

arquivo = "dados.json"

lista_cadastros = []
arquivo_aberto = open(arquivo, "r", encoding="utf-8")
lista_cadastros= json.load(arquivo_aberto)
arquivo_aberto.close() 

while True:
    print("Administração pública")
    print("Escolha opção")
    print("1 - Cadastrar")
    print("2 - Exibir")
    print("3 - Editar")
    print("4 - Deletar")
    print("5 - Pesquisar")
    print("6 - Gerar relatorio")
    print("0 - Sair")

    opcao = input("Insira opção\n")
    if opcao == "1":
        print("parte do cadastro")
        #parte d qm for fazer o cadastro

    elif opcao == "2":
        print("parte de exibir")
        ##parte d qm for fazer o exibir

    elif opcao == "3":
        print("parte de editar")
        #parte d qm for fazer a edicao

    elif opcao == "4":
        print("parte de deletar")
        #parte d qm for fazer o delete

    elif opcao == "5":
        print("parte de pesquisa")
        ##parte d qm for fazer a pesquisa

    elif opcao == "6":
        print("parte de gerar o relatorio")
        ##parte d qm for fazer o relatorio

    elif opcao == "0":
        print("parte de sair")
        break
    else:
        print("opcao invalido")