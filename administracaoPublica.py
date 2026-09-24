# -*- coding: utf-8 -*-
import json

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
        
        nome = input("Nome: ").strip()
        
        tem_numero = False
        for letra in nome:
            if letra in "0123456789":
                tem_numero = True
                break
        
        if tem_numero:
            print("Erro: o nome não pode conter números.")
        else:
            cargo = input("Cargo: ").strip()
            orgao = input("Órgão / Secretaria: ").strip()
            matricula = input("Matrícula: ").strip()
        
            if nome == "" or cargo == "" or orgao == "" or matricula == "":
                print("Erro: preencha todos os campos.")
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

   
    elif opcao == "2":
        print("parte de exibir")

##parte d qm for fazer o exibir

    elif opcao == "3":
      arq = open('dados.json', 'r', encoding='utf-8')
      dados = json.load(arq)
      arq.close()
            
    print('\n Editar servidor publico')
    id_editar = input('Digite o ID do servidor: ')
            
    encontrado = False 
            
    for servidor in dados:
                if str(servidor['id']) == id_editar:
                    print('Nome atual:', servidor['nome'])
                    print('Cargo atual:', servidor['cargo'])
                    print('Órgão atual:', servidor['orgao'])
                    print('Matrícula atual:', servidor['matrícula'])
                    
                    servidor['nome'] = input('Novo nome: ')
                    servidor['cargo'] = input('Novo cargo: ')
                    servidor['orgao'] = input('Novo órgão: ')
                    servidor['matrícula'] = input('Nova matrícula: ')
                    
                    arq = open('dados.json', 'w', encoding='utf-8')
                    json.dump(dados, arq, ensure_ascii=False, indent=4)
                    arq.close()
                    print('Servidor editado com sucesso.')
                    
                    encontrado = True
                    break
                    
    if encontrado == False:
                print('ID não encontrado.')
    elif opcao == "4":
     print("parte de deletar")

##parte d qm for fazer o delete
    elif opcao == "5":
                    print("parte de pesquisa")

##parte d qm for fazer a pesquisa

    elif opcao == "6":

                    print("parte de gerar o relatorio")

##parte d qm for fazer o relatorio



    elif opcao == "0":

                    print("parte de sair")

    break

else:

     print("opcao invalido")


