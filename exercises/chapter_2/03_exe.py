def verifica_nota(nota):
    
    if(nota >= 0.9 and nota<=1.0):
        return "A"
    
    elif(nota >= 0.8 and nota < 0.9):
        return "B"
    
    elif(nota >= 0.7 and nota < 0.8):
        return "C"
    
    elif(nota >= 0.6 and nota < 0.7):
        return "D"
    
    elif(nota >= 0 and nota < 6):
        return "F"       
    
    else:
        return "Pontuação Inválida"
    
def main():
    print("Sistema classifica nota por pontuação")
    try:
        pontuacao = float(input("Digite a pontuação: "))    
        print(verifica_nota(pontuacao))
    
    except:
        print("Pontuação Inválida")

main()