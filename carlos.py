
#opçao6
def gerar_relatorio():
    arq = open("dados.json", "r", encoding="utf-8")
    dados = json.load(arq) # Abre o arquivo JSON e carrega os dados dos servidores em uma variável

    arq.close()

    relatorio = open("relatorio.txt", "w", encoding="utf-8")
    relatorio.write("RELATÓRIO DE SERVIDORES\n")
    relatorio.write("========================\n\n") #cria um relatorio .txt

    for servidor in dados:
        relatorio.write(f"ID: {servidor['id']}\n")
        relatorio.write(fNome: {servidor['nome']}\n")
        relatorio.write(f"Cargo: {servidor['cargo']}\n")
        relatorio.write(f"Órgão: {servidor['orgao']}\n")
        relatorio.write(f"Matrícula: {servidor['matricula']}\n)
        relatorio.write("------------------------\n")#escreve no relatorio usando f-string

    relatorio.close()

    print("Relatório gerado com sucesso!")

elif opcao == "0":
    print("Saindo do sistema...")s
    break 
#quebra o laço de repetiçao do começo do codigo
#NOTA: não pude compararecer a aula hoje por motivos de doença, por favor dar uma olhada no codigo, 
#para que eu possa  corrigir e colocar no main, obrigado
