def main():
    path = "archives/mbox-short.txt"
    arquivo = open(path)
    for linha in arquivo:
        linha = linha.rstrip()
        #SKIP O QUE NÃO SATISFAZ A CONDIÇÃO LINHAS QUE NÃO INICIALIZA COM FROM SÃO PULADAS
        if not linha.startswith("From"):
            continue
        
        #IMPRIME SOMENTE O QUE REALMENTE INTERESSA
        print(linha)
main()