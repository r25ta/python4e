from os import write


def main():
    dir = "archives/"
    
    arq_name = input("Digite o nome do arquivo de entrada >>")
    keyword = input("Digite a palavra a ser pesquisada >>")
    saida=[]
    arquivo_entrada = open(dir+arq_name)
    for linha in arquivo_entrada:
        linha = linha.rstrip()
    
        if linha.find(keyword)!=-1:
            saida.append(linha)
    
    if len(saida) > 0:
        print("No arquivo %s ,foram encontradas %d ocorrências da palavra %s" %(dir+arq_name, len(saida), keyword))

        isExport = input("Deseja exportar essa informação? (S/N) >>")
        if isExport=="S":
            arq_saida = input("Digite o nome do arquivo >>")
            arq_export = open(dir+arq_saida,'w')
            for linha_export in saida:
                arq_export.write(linha_export+"\n")
            
            arq_export.close()
    else:
        print("No arquivo %s ,não foram encontradas ocorrências da palavra %s" %(dir+arq_name, keyword))
        
main()