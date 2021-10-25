def main():
    path = 'archives/mbox-short.txt'
    arquivo = open(path)
    conteudo = arquivo.read()
    linhas = len(conteudo)
    print("O arquivo tem %d linhas" %(linhas))
    
    print("Exibir os 20 primeiros caracteres do arquivo")
    print(conteudo[:20])
     
    
main()