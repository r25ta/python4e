import string

def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_9/archives/"
    arq_name = input("Digite o nome do arquivo: ")
    dic_server = dict()
    
    try:
        arquivo = open(path+arq_name)
    
    except:
        print("Arquivo %s não encontrado, tente novamente!")
        exit()
        
    for line in arquivo:
        line = line.rstrip()
        if line.startswith("From"):
            palavras = line.split()
            if len(palavras) >= 1:
                servidor = palavras[1]
                servidor = servidor[ servidor.find("@") +1 : ]
                
                if servidor not in dic_server:            
                    dic_server[servidor] = 1
                
                else:
                    dic_server[servidor] += 1
                    
    print(dic_server)
                
main()