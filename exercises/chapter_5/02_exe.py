def laco_maximo():
    maximo = None
    print("Antes:",maximo)
    
    for itervar in [3,41,12,9,74,15]:
        if maximo == None or itervar > maximo:
            maximo = itervar
            
        print("Compara => Itervar:",itervar," Máximo:",maximo)
    
    print("Máximo:",maximo)
    
def laco_minimo():
    minimo = None
    print("Antes",minimo)
    
    for itervar in [3,41,12,9,74,15]:
        if minimo == None or itervar < minimo:
            minimo = itervar
            
        print("Compara => Itervar:",itervar," Minimo:",minimo)
    
    print("Minimo:", minimo) 
    
    
def main():
    print("\nLocaliza maior número da lista")
    laco_maximo()
    print("\nLocaliza menor número da lista")
    laco_minimo()
    
main()