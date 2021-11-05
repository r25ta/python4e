def main():
    counts = {"Ronaldo":42,"Olivia":40,"Diego":11,"Camila":7,"Luna":1}
    #Metodo KEY() retorna uma lista de chaves
    lst = list(counts.keys())
    print(lst)
    #Dessa forma é possivel ordernar a lista
    lst.sort()
    
    for key in lst:
        #IMprime chave e conteudo do dicionario em ordem alfabetica
        print(key,counts[key])
    
main()