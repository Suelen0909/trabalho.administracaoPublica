
arq = open('dados.json', 'r', encoding='utf-8')
dados = json.load(arq)
arq.close()

if len(dados) == 0:
            print("Não existem servidores cadastrados.")

else:
            print('\n Editar servidor publico')

            id_editar = input('Digite o ID do servidor: ')

            encontrado = False

            for servidor in dados:

                if str(servidor['id']) == id_editar:

                    print('Nome atual:', servidor['nome'])
                    print('Cargo atual:', servidor['cargo'])
                    print('Órgão atual:', servidor['orgao'])
                    print('Matrícula atual:', servidor['matricula'])

                    servidor['nome'] = input('Novo nome: ')
                    servidor['cargo'] = input('Novo cargo: ')
                    servidor['orgao'] = input('Novo órgão: ')
                    servidor['matricula'] = input('Nova matrícula: ')

                    encontrado = True

                    break

            if encontrado == True:

                arq = open('dados.json', 'w', encoding='utf-8')
                json.dump(dados, arq, ensure_ascii=False, indent=4)
                arq.close()

                print('Servidor editado com sucesso.')

            else:

                print('ID não encontrado.')
   