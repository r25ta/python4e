#EXERCISES COMPARE TUPLE
#OS OPERADORES DE COMPARAÇÃO TRABALHAM COM TUPLAS E OUTRAS SEQUENCIAS.
#PYTHON COMEÇA COMPARANDO O PRIMEIRO ELEMENTO DE CADA SEQUENCIA.
#SE ELES FOREM IGUAIS ELE PASSA PARA O PRÓXIMO ELEMENTO, E ASSIM POR DIANTE,
#ATÉ ENCONTRAR ELEMENTOS QUE DIFEREM. ELEMENTOS SUBSEQUENTES NÃO SÃO CONSIDERADOS

def first_comparison():
    elements_1 = (1,2,3,4,5,)
    elements_2 = (1,2,3,4000,5000)
    print("\nTuple elements_1",elements_1)
    print("\nTuple elements_2",elements_2)
    print("\nelements_1 is greater than elements_2 equal", elements_1 > elements_2 )

def second_comparison():
    elements_1 = (1,2,3,4,5,)
    elements_2 = (1,2,3,4000,5000)

    print("\nTuple elements_1",elements_1)
    print("\nTuple elements_2",elements_2)
    print("\nelements_2 is greater than elements_1 equal", elements_2 > elements_1 )

#UTILIZAÇÃO DA FUNÇÃO SORT, ATRAVES DO PADRÃO DSU
#D = DECORAR: UMA SEQUENCIA CONSTRUINDO UMA LISTA DE TUPLAS COM UMA OU MAIS CHAVES DE CLASSIFICAÇÃO
#S = SORT: A LISTA DE TUPLAS USANDO A FUNÇÃO SORT
#U = UNDECORATE: EXTRAINDO OS ELEMENTOS CLASSIFICADOS DA SEQUENCIA
def sort_word_largest_smallest():
    print("\nAlgoritimo para ordenar palavras na forma decrescente utilizando padrão DSU")
    #TEXTO CONTENTO DIVERSAS PALAVRAS
    txt = "Ronaldo Camila Diego Olivia Luna Soldado Antonio Patrocinio Fernandes"
    print("Texto original com as palavras a serem ordenadas",txt)
    #DECLARAÇÃO DA LISTA
    t = list()
    #TRANSFORMANDO TEXTO EM UMA LISTA DE PALAVRAS
    words = txt.split()
    print("Texto original transformado em list de palavras",words)
    #AQUI ENTRA A LETRA D(DECORAR) DO PADRÃO DSU
    for word in words:
        #CADA ELEMENTO DA LISTA POSSUI O TAMANHO DA PALAVRA, ANTES DA PALAVRA
        t.append((len(word),word))

    print("Lista de palavras concatenadas com o se respectivo tamanho",t)
    #AQUI ENTRA A LETRA S(SORT) DO PADRÃO DSU
    #ORDENA DO MAIOR PARA MENOR (REVERSE = TRUE)
    t.sort(reverse=True)
    print("lista de palavras ordenadas de forma decrescente",t)
    ret = list()
    #AQUI ENTRA A LETRA U(UNDECORATE) DO PADRÃO DSU
    for size, word in t:
        #PARA CADA ELEMENTO DA NOVA LISTA É RETIRADO O TAMANHO DA PALAVRA QUE FOI USADO PARA ORDENAÇÃO
        ret.append(word)

    #IMPRIME APENAS AS PALAVRAS POR ORDEM DE TAMANHO DECRESCENTE
    print("Produto final lista de palavras ordenadas de forma decrescente",ret)


if __name__ == "__main__":
    first_comparison()
    second_comparison()
    sort_word_largest_smallest()