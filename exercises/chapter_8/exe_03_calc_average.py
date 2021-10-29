def main():
    lstTotal=[]
    while (True):
        print("Para Sair para encerrar")
        entrada = input("Digite um número:")
        if entrada == "sair":
            break
        
        lstTotal.append(float(entrada))
        print(sum(lstTotal))
    try:    
        media = sum(lstTotal) / len(lstTotal)
        print("Média",media)
    
    except:
        print("Não foi possivel calcular a média")
        
    
    
    
main()