def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_7/archives/"
    nom_arq = input("Digite o nome do arquivo: ")
    try:
        arquivo = open(path+nom_arq)
    except:
        print("Nome de arquivo invalido, tente novamente")
            
    for linha in arquivo:
        palavras = linha.split()
        if len(palavras) == 0 or palavras[0] != "From":
            continue
        
        print(palavras[2])
main()