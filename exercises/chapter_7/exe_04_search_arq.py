def main():
    path = 'archives/mbox-short.txt'
    arquivo = open(path)
    
    for linha in arquivo:
        #INSTRUÇÃO PARA RETIRAR O ESPAÇO EM BRANCO NO FINAL DA LINHA
        linha = linha.rstrip
        #LOCALIZA LINHAS QUE INICIALIZA COM FROM
        if linha.startswith("From"):
            print(linha)
    
    
main()