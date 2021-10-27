def main():
    dir = "archives/"
    try:
        arq_name = input("Digite o nome do arquivo >>")
        arq = open(dir+arq_name)
        
        for line in arq:
            line = line.rstrip()
            print(line.upper())
        
    except:
        print("Arquivo não encontrado!")
        exit()
        
main()