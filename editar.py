import json

arq = open('dados.json', 'r', encoding='utf-8')
dados = json.load(arq)
arq.close()

print("editar servidor")

id_editar = input("Digite o ID do servidor: ")

for servidor in dados:
    if str(servidor['id']) == id_editar:

        print("Nome atual:", servidor['nome'])
        print("Cargo atual:", servidor['cargo'])
        print("Órgão atual:", servidor['orgao'])
        print("Matrícula atual:", servidor['matricula'])

        servidor['nome'] = input("Novo nome: ")
        servidor['cargo'] = input("Novo cargo: ")
        servidor['orgao'] = input("Novo órgão: ")
        servidor['matricula'] = input("Nova matrícula: ")