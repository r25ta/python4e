def comprimento(str):
    print("A palavra",str, "tem",len(str)," caracteres")

def obterUltimaLetra(str):
    print("Pode se obter a ultima letra str[len(str) - 1] =>",str[len(str)-1])
    print("\n ou utilizar -1 para retornar a ultima letra str[-1] =>",str[-1])
    
def travessia(str):
    idx = 0
    while idx < len(str):
        letra = str[idx]
        print(letra)
        idx = idx+1
        
def main():
    flag = True
    while flag:
        print("Funções da classe String")
        palavra = input("Digite uma palavra, ou digite sair para sair: ")
        if palavra == "sair":
            flag=False
        
        comprimento(palavra)
        obterUltimaLetra(palavra)
        travessia(palavra)        
        
main()