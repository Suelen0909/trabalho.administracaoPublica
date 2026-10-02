
arq = open('dados.json', 'r', encoding='utf-8')
dados = json.load(arq)
arq.close()

if len(dados) == 0:

    print("Não existem servidores cadastrados.")

else:

            id_deletar = input("Digite o ID do servidor: ")

            encontrado = False

            for i in range(len(dados)):

                if str(dados[i]['id']) == id_deletar:

                    print("ID:", dados[i]['id'])
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

                        print("Servidor deletado com sucesso.")

                    elif confirmacao == 'N' or confirmacao == 'n':

                        print("Operação cancelada.")

                    else:

                        print("Opção inválida. Digite S ou N.")

                    encontrado = True

                    break

            if encontrado == False:

                print("ID não encontrado.")