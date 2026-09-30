 if opcao == "1":
       
    dados = []

    arq = open('dados.json', 'a', encoding='utf-8')
    arq.close()

    arq = open('dados.json', 'r', encoding='utf-8')
    conteudo = arq.read().strip()
    arq.close()

    if conteudo == "":
        dados = []
    else:
        arq = open('dados.json', 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()

    if len(dados) > 0:
        proximo_id = dados[-1]['id'] + 1
    else:
        proximo_id = 1

        print("\n=== CADASTRAR SERVIDOR PÚBLICO ===")
        print("ID:", proximo_id)

        tem_numero = False

        nome = input("Nome: ").strip()

        if nome == "":
            print("Erro: o nome não pode ficar em branco.")
        else:
            for letra in nome:
                if letra in "0123456789":
                    tem_numero = True
                    break

            if tem_numero:
                print("Erro: o nome não pode conter números.")
            else:
                cargo = input("Cargo: ").strip()
                if cargo == "":
                    print("Erro: o cargo não pode ficar em branco.")
                else:
                    orgao = input("Órgão / Secretaria: ").strip()
                    if orgao == "":
                        print("Erro: o órgão não pode ficar em branco.")
                    else:
                        matricula = input("Matrícula: ").strip()
                        if matricula == "":
                            print("Erro: a matrícula não pode ficar em branco.")
                        else:
                            novo = {
                                "id": proximo_id,
                                "nome": nome,
                                "cargo": cargo,
                                "orgao": orgao,
                                "matricula": matricula
                            }
                            dados.append(novo)
                            arq = open('dados.json', 'w', encoding='utf-8')
                            json.dump(dados, arq, ensure_ascii=False, indent=4)
                            arq.close()
                            print("Servidor cadastrado com sucesso.")