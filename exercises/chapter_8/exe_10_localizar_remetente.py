def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_7/archives/"
    arq = input("Digite o nome do arquivo: ")
    try:
        arquivo = open(path+arq)
    except:
        print("Arquivo não encontrado, favor tentar novamente")
    
    cont = 0
    for linha in arquivo:
        if linha.startswith("From"):
            palavras = linha.split()
            print(palavras[1])
            cont +=1

    print("O arquivo possui %d linhas com a palavra From" %(cont)) 
main()        