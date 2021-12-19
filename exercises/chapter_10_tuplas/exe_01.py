#EXERCICIO 1 => TUPLAS TIPOS DE DECLARAÇÃO

def declare_many_elements():
    #TUPLA É SEMELHANTE A UMA LISTA,A DIFERENÇA É QUE OS VALORES DAS TUPLAS SÃO IMUTAVEIS
    #PARA DIFERENCIAR AS TUPLAS DAS LISTAS, É COMUM INCLUIR PARENTESES
    tupla = ('a','b','c','d','f','g','h',)
    print("Tupla com varios elementos", tupla, "=>", type(tupla))

def declare_one_element():
    #Tupla com apenas UM elemento, deve ter virgula no final
    tupla = ('A',)
    print("Tupla com UM elemento ",tupla, "=>", type(tupla))

def declare_usage_tuple_function():
    tupla = tuple('Opala SS')
    print("Tupla declarada com função tuple() passando String OpalaSS ", tupla, "=>", type(tupla))

    elements = ['a','b','c','d']
    t = tuple(elements)
    print("Tupla declarada com função tuple(), passando uma List",elements, type(elements) , " | Tupla " ,t, type(t))

if __name__ == "__main__":
    declare_one_element()
    declare_many_elements()
    declare_usage_tuple_function()
