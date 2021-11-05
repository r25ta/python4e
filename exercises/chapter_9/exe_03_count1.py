def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_9/archives/"
    
    nom_arq = input("Digite o nome do arquivo: ")
    try:
        arquivo = open(path+nom_arq)
        
    except:
        print("Arquivo invalido, tente novamente")
        exit    
    countPalavra = dict()
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            if palavra not in countPalavra:
                countPalavra[palavra] = 1
            else:
                countPalavra[palavra] += 1
        
    print(countPalavra)
    
main()