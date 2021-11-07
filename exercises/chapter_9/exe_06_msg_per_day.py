def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_9/archives/"
    
    arq_name = input("Digite o nome do arquivo: ")
    dict_palavras = dict()
    try:
        arquivo = open(path+arq_name)
    
    except:
        print("O arquivo %s não existe, tente novamente!" % (arq_name))
        exit()
        
    for linha in arquivo:
        linha = linha.rstrip()
        if linha.startswith("From"):
            palavras = linha.split()
            if len(palavras)>=3:
                if palavras[2] not in dict_palavras:
                    dict_palavras[palavras[2]] = 1
                
                else:
                    dict_palavras[palavras[2]] +=1
                      
    print(dict_palavras)
            
            
main()