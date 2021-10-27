def main():
    dir = "archives/"
    try:
        arq_name = input("Digite o nome do arquivo >>")
        arq = open(dir+ arq_name)
    except:
        print("Nome de arquivo inválido!")
        exit()
        
    count = 0
    for line in arq:
        if line.startswith("Subject:"):
            count +=1
            
    print("O arquivo %s possui %d linhas com a palavra Subject" % (dir+arq_name, count))
        
main()