while True:

    print ("Administração pública\n")

    print ("Escolha opção")

    print ("1 - Cadastrar")

    print ("2 - Exibir")

    print("3 - Editar")

    print("4 - Deletar")

    print("5 - Pesquisar")

    print("6 - Gerar relatorio")

    print("0 - Sair")



    opcao = input("Insira opção: ")

    if opcao == "1":
        print("parte do cadastro")

##parte d qm for fazer o cadastro

    elif opcao == "2":
        print("parte de exibir")


    arq = open('dados.json', 'r', encoding='utf-8')
    conteudo = arq.read().strip()
    arq.close()

    if conteudo == "":
        print("Nenhum servidor cadastrado.")

    else:
        arq = open('dados.json', 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()

        print("\n=== SERVIDORES CADASTRADOS ===")

        for servidor in dados:
            print("ID:", servidor["id"])
            print("Nome:", servidor["nome"])
            print("Cargo:", servidor["cargo"])
            print("Órgão / Secretaria:", servidor["orgao"])
            print("Matrícula:", servidor["matricula"])
            print("-" * 30)


    

##parte d qm for fazer o exibir

    elif opcao == "3":
        print("parte de editar")

##parte d qm for fazer a edicao
    elif opcao == "4":
        print("parte de deletar")

##parte d qm for fazer o delete
    elif opcao == "5":
            elif opcao == "5":

    arq = open('dados.json', 'r', encoding='utf-8')
    conteudo = arq.read().strip()
    arq.close()

    if conteudo == "":
        print("Nenhum servidor cadastrado.")

    else:
        arq = open('dados.json', 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()

        id_busca = int(input("Digite o ID do servidor: "))

        encontrado = False

        for servidor in dados:

            if servidor["id"] == id_busca:

                print("\n=== SERVIDOR ENCONTRADO ===")
                print("ID:", servidor["id"])
                print("Nome:", servidor["nome"])
                print("Cargo:", servidor["cargo"])
                print("Órgão / Secretaria:", servidor["orgao"])
                print("Matrícula:", servidor["matricula"])

                encontrado = True

        if encontrado == False:
            print("Servidor não encontrado.")


##parte d qm for fazer a pesquisa



    elif opcao == "6":

        print("parte de gerar o relatorio")

##parte d qm for fazer o relatorio



    elif opcao == "0":

        print("parte de sair")

        break

    else:

         print("opcao invalido")

