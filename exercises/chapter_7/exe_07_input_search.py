def main():
    dir = "archives/"
    arq_name = input("Digite o nome do arquivo:")
    
    arquivo = open(dir+arq_name)
    
    for linha in arquivo:
        linha = linha.rstrip()
        if linha.startswith("From"):
            print(linha)
        
main()