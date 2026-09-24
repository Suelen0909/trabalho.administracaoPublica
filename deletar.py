import json
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

if len(dados) == 0:
            print("Não existem servidores cadastrados.")

else:
            print('\n=== DELETAR SERVIDOR PÚBLICO ===')

            id_deletar = input('Digite o ID do servidor: ')

            encontrado = False

            for servidor in dados:

                if str(servidor['id']) == id_deletar:

                    print('ID:', servidor['id'])
                    print('Nome:', servidor['nome'])
                    print('Cargo:', servidor['cargo'])
                    print('Órgão:', servidor['orgao'])
                    print('Matrícula:', servidor['matricula'])

                    confirmacao = input('Tem certeza que deseja deletar? (S/N): ')

                    if confirmacao == 'S' or confirmacao == 's':

                        dados.remove(servidor)

                    arq = open('dados.json', 'w', encoding='utf-8')
                    json.dump(dados, arq, ensure_ascii=False, indent=4)
                    arq.close()

                    print('Servidor deletado com sucesso.')

                elif confirmacao == 'N' or confirmacao == 'n':

                    print(' servidor deletado .')

                else:

                    print('Opção inválida. Digite S ou N.')