def main():
    path = 'archives/mbox.txt'
    arquivo = open(path)
    contador = 0
    for linha in arquivo:
        contador = contador + 1
    
    print("O arquivo tem %d linhas" %(contador))
    
    
    
main()