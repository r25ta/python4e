def main():
    path="archives/mbox-short.txt"
    arquivo = open(path)
    for linha in arquivo:
        linha=linha.rstrip()
        #IGNORA TODAS AS LINHAS QUE NÃO SATISFAZ A CONDIÇÃO A SEGUIR
        if linha.find("@uct.ac.za")==-1:
            continue
        
        #IMPRIME SOMENTE AS LINHAS RELEVANTES
        print(linha)
    
main()