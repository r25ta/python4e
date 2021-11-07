import string

def main():
    path = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_9/archives/"
    arq_name = input("Digite o nome do arquivo: ")
#INICIALIZA UM DICIONARIO    
    dic_palavras = dict()
    try:
        arquivo = open(path+arq_name)
        
    except:
        print("O arquivo %s não existe, tente novamente!" % (arq_name) )
        exit()
                
    for linha in arquivo:
    #RETIRA OS ESPAÇO EM BRANCO NO FINAL DA LINHA
        linha = linha.rstrip()
    #RETIRA POTUAÇÃO DAS PALAVRAS
    #TRANSLATE() REALIZA UM SUBSTITUIÇÃO, RECEBE COMO PARAMETRO UM DICT OU TABLE
    #STRING.PUNCTUATION RETORNA DOS OS CARARTERES DE PONTUAÇÃO
        linha = linha.translate(linha.maketrans('','',string.punctuation))
    #ALTERAR TODAS AS PALAVRAS DA LINHA PARA LOWER CASE
        linha = linha.lower()
    #QUEBRA A LINHA EM PALAVRAS E RETORNA UMA LISTA DE PALAVRAS
        palavras = linha.split()
        for palavra in palavras:
            #CONTADOR DE REPETIÇÕES DE PALAVRAS NO TEXTO
            if palavra not in dic_palavras:
                dic_palavras[palavra] = 1
            
            else:        
                dic_palavras[palavra] += 1
                
    print(dic_palavras)
    
main()