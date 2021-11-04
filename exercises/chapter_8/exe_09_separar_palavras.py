def main():
    arquivo = open("/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_8/romeo/romeo.txt")
    palavra_unica=[]
    
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            if palavra not in palavra_unica:
                palavra_unica.append(palavra)
        
        
    arquivo.close()
    palavra_unica.sort()
    print(palavra_unica)
main()