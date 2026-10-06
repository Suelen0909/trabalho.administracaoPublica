    elif opcao == "2":

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

