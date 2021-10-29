def main():
    queijos = ["Chedar","Prato","Muzarella","Provolone","Gouda","Brie","Minas"]
    numeros=[13,23,45,1,89,50,100,98,87]
    empty=[]
    print(queijos)
    print(numeros)
    print(empty)

    mudarValorLista(numeros,3,99)

def mudarValorLista(lista, id, valor):
    print("Valor do ID %d na lista antes da mudança: %d" % (id, lista[id]))
    print(lista)
    lista[id] = valor
    print("Valor do ID %d depois da mundança da lista %d" % (id, lista[id]))
    print(lista)
main()