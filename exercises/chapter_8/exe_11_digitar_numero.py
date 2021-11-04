def main():
    flag = True
    lst = []
    while flag:
        str_n = input("Digite um número ou done para sair: ")
        if str_n.lower() == "done":
            flag = False
            if(len(lst)>0):
                print("Máximo ", max(lst))
                print("Minimo ",min(lst))
                print("Média", sum(lst)/ len(lst))
        
        try:
            n = float(str_n) 
            lst.append(n)
        except:
            if str_n.lower() != "done":
                print("Favor digite um numero valido") 
                
main()        
          
        
        