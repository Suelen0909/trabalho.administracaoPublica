arq = open('dados.json', 'r', encoding='utf-8')
dados = json.load(arq)
arq.close()

id_deletar = input("Digite o ID do servidor: ")

encontrado = False

for servidor in dados:

            if str(servidor['id']) == id_deletar:

                encontrado = True

                print("ID:", servidor['id'])
                print("Nome:", servidor['nome'])
                print("Cargo:", servidor['cargo'])
                print("Órgão:", servidor['orgao'])
                print("Matrícula:", servidor['matricula'])

                confirmacao = input(
                    "Tem certeza que deseja deletar? (s/n): "
                ).lower()

                if confirmacao == "s":

                    dados.remove(servidor)

                    arq = open('dados.json', 'w', encoding='utf-8')
                    json.dump(dados, arq, ensure_ascii=False, indent=4)
                    arq.close()

                    print("Servidor deletado com sucesso.")

                else:
                    print("Operação cancelada.")

                break

if encontrado == False:
            print("ID não encontrado.")