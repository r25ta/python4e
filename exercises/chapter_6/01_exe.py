#Travessia Contrária com While
def travessiaContrariaWhile(str):
    idx = len(str)-1
    
    while idx >= 0:
        print(str[idx])
        idx = idx - 1

#Travessia Contrária com For        
def travessiaContrariaFor(str):
    
    idx = len(str)-1
    for idx in range(idx,-1,-1):
        print(str[idx])


    
def main():
    palavra = input("Digite uma palavra: ")
    
    travessiaContrariaWhile(palavra)
    travessiaContrariaFor(palavra)
main()