# -*- coding: utf-8 -*-
import json


while True:


    print ("\nAdministração pública\n")


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
                            print("\nServidor cadastrado com sucesso.")


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


        print("\n=== SERVIDORES CADASTRADOS ===\n")


        for servidor in dados:
            print("ID:", servidor["id"])
            print("Nome:", servidor["nome"])
            print("Cargo:", servidor["cargo"])
            print("Órgão / Secretaria:", servidor["orgao"])
            print("Matrícula:", servidor["matricula"])
            print("-" * 30)


    elif opcao == "3":


        arq = open('dados.json', 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()


        if len(dados) == 0:
            print("Não existem servidores cadastrados.")


        else:
            print('\nEditar servidor publico\n')


            id_editar = input('Digite o ID do servidor: ')


            encontrado = False


            for servidor in dados:


                if str(servidor['id']) == id_editar:


                    print('Nome atual:', servidor['nome'])
                    print('Cargo atual:', servidor['cargo'])
                    print('Órgão atual:', servidor['orgao'])
                    print('Matrícula atual:', servidor['matricula'])


                    servidor['nome'] = input('\nNovo nome: ')
                    servidor['cargo'] = input('Novo cargo: ')
                    servidor['orgao'] = input('Novo órgão: ')
                    servidor['matricula'] = input('Nova matrícula: ')


                    encontrado = True


                    arq = open('dados.json', 'w', encoding='utf-8')
                    json.dump(dados, arq, ensure_ascii=False, indent=4)
                    arq.close()


                    print('\nServidor editado com sucesso.')


                    break


            if encontrado == False:


                print('ID não encontrado.')

    elif opcao == "4":

        arq = open('dados.json', 'r', encoding='utf-8')
        dados = json.load(arq)
        arq.close()


        if len(dados) == 0:


            print("Não existem servidores cadastrados.")


        else:


            id_deletar = input("\nDigite o ID do servidor: ")


            encontrado = False


            for i in range(len(dados)):


                if str(dados[i]['id']) == id_deletar:


                    print("\nID:", dados[i]['id'])
                    print("Nome:", dados[i]['nome'])
                    print("Cargo:", dados[i]['cargo'])
                    print("Órgão:", dados[i]['orgao'])
                    print("Matrícula:", dados[i]['matricula'])


                    confirmacao = input(
                        "Tem certeza que deseja deletar? (S/N): "
                    )


                    if confirmacao == 'S' or confirmacao == 's':


                        dados.pop(i)


                        arq = open('dados.json', 'w', encoding='utf-8')
                        json.dump(dados, arq, ensure_ascii=False, indent=4)
                        arq.close()


                        print("\nServidor deletado com sucesso.")


                    elif confirmacao == 'N' or confirmacao == 'n':


                        print("Operação cancelada.")

                    else:

                        print("Opção inválida. Digite S ou N.")

                    encontrado = True

                    break

            if encontrado == False:

                print("ID não encontrado.")

    elif opcao == "5":


        arq = open('dados.json', 'r', encoding='utf-8')
        conteudo = arq.read().strip()
        arq.close()


        if conteudo == "":
            print("\nNenhum servidor cadastrado.")


        else:
            arq = open('dados.json', 'r', encoding='utf-8')
            dados = json.load(arq)
            arq.close()


        id_busca = int(input("\nDigite o ID do servidor: "))


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


    elif opcao == "6":
        with open('dados.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
       
            with open('relatorio.txt', 'w', encoding='utf-8') as relatorio:
                relatorio.write('RELATÓRIO DE SERVIDORES\n')
                relatorio.write('========================\n\n')
       
                for servidor in dados:
                    relatorio.write(f"ID: {servidor['id']}\n")
                    relatorio.write(f"Nome: {servidor['nome']}\n")
                    relatorio.write(f"Cargo: {servidor['cargo']}\n")
                    relatorio.write(f"Órgão: {servidor['orgao']}\n")
                    relatorio.write(f"Matrícula: {servidor['matricula']}\n")
                    relatorio.write('------------------------\n')
           
        print('\nRelatório gerado com sucesso!')
    elif opcao == "0":
        print("\nSaindo do sistema...")
        break

else:

    print("opcao invalido")
