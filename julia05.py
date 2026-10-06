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
