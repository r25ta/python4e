def corte(lst):
    lst.pop(0)
    lst.pop(len(lst)-1)
    print("dentro do metodo Corte", lst)

def meio(lst):
    return lst[1:len(lst)-1]

def main():
    t = [1,2,3,4,5,6,7,8,9,0]
    print("Lista criada", t)
    corte(t)
    print("Saida do metodo corte",t)

    t1 = [0,9,8,7,6,5,4,3,2,1]
    print("Lista criada", t1)
    corte(t1)
    print("Saida do metodo meio",t1)
    

main()