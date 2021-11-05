def main():
    familia = {"ronaldo":43, "olivia":40, "diego":11, "camila":7}
    #METODO GET RETORNA O VALOR DA CHAVE, E SENÃO ENCONTRAR RETORNA O VALOR PADRÃO
    #CHAVE RONALDO, VALOR 43
    print(familia.get("ronaldo",0))
    #CHAVE LUNA, NÃO EXISTE VALOR O METODO GET ASSUME 0 VALOR DEFINIDO COMO PADRAO
    print(familia.get("luna",0)) 
    
main()   