#IMPORTAÇÃO DO PACOTE OS PARA PECORRER DIRETÓRIOS
import os

def main():
    slash="/"
    #METODO PATH.ABSPATH RETORNAR O CAMINHO ABSOLUTO
    dir = os.path.abspath("../chapter_7/archives/")
    
    arq_name = input("Digite o nome do arquivo: ")
    try:
        arquivo = open(dir+slash+arq_name)

    except:
        print("Arquivo não encontrado")
        exit()

    lst_spans = []
    for linha in arquivo:
        linha = linha.rstrip()
        if linha.startswith("X-DSPAM-Confidence"):
            #TRANSFORMA O CONTEUDO DA LISTA DE STRING PARA FLOAT
            lst_spans.append(float(linha[20:]))
    #MEDIA SUM DA LISTA DIVIDIDO PELO LEN DA LISTA
    average = sum(lst_spans) / len(lst_spans)
    
    print("Média de confiança de spam: %g" % (average))
        
main()