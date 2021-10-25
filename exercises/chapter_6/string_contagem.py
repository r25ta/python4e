def contagem(palavra, letra):
    contador = 0
    for l in palavra:
        if letra == l:
            contador = contador + 1
    
    print("Na palavra ", palavra, " tem ", contador, " ocorrencias com a letra", letra)
    
def  main():
    palavra = input("Digite uma palavra:")
    letra = input("Digite a letra:")
    
    contagem(palavra, letra)
    
main()    