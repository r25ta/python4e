import string

def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_9/archives/"
    arq_name = input("Digite o nome do arquivo: ")
    dic_emails= dict()
        
    try:
        arquivo = open(path+arq_name)
        
    except:
        print("Arquivo %s não encontrado" % (arq_name))
        exit()
        
    for linha in arquivo:
        linha = linha.rstrip()
        if linha.startswith("From"):
            linha = linha.lower()
            linha.translate(str.maketrans('','',string.punctuation))
            palavras = linha.split()
            if len(palavras)>=1 and palavras[1].find("@"):
#                print("email", palavras[1])

                if palavras[1] not in dic_emails:    
                    dic_emails[palavras[1]] = 1
                
                else:
                    dic_emails[palavras[1]] += 1

    print(dic_emails) 
    
# QUEM RECEBEU MAIS EMAIL
    valor_maior = 0
    valor_menor = 0
    idx_maior=None
    idx_menor=None
        
    for idx in dic_emails:
        print(idx,dic_emails[idx])
        if (dic_emails[idx]>valor_maior):
            valor_maior = dic_emails[idx]
            idx_maior = idx
            
    
        if (valor_menor==0 or dic_emails[idx]<valor_menor):
            valor_menor = dic_emails[idx] 
            idx_menor = idx
                        
    print("Usuário que mais recebeu e-mail: ",idx_maior,dic_emails[idx_maior])
    print("Usuário que menos recebeu email: ",idx_menor,dic_emails[idx_menor])       
            
            
# QUEM RECEBEU MENOS EMAIL
       
       
main()