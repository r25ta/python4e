from motorista import Motorista
import pandas as pd

path_arq = "/home/ronaldo/_DESENVOLVIMENTO/Python/python4e/exercises/chapter_8/Telerisco/base_telerisco/Planilha_Motoristas_Teste_Novo_Telerisco.xlsx"
fonte_dados = pd.read_excel(path_arq, sheet_name="Frota-Agregado")

motoristas = fonte_dados[["CPF_MOTORISTA","NOME_MOTORISTA","CNPJ TRANSPORTADORA", "NOME TRANSPORTADORA","CNPJ OPERAÇÃO","NOME OPERAÇÃO"]]

lst_motoristas =[]
for m in motoristas.iterrows():
    motorista = Motorista(m[1].get("CPF_MOTORISTA")
                         ,m[1].get("NOME_MOTORISTA")
                         ,m[1].get("CNPJ TRANSPORTADORA")
                         ,m[1].get("NOME TRANSPORTADORA")
                         ,m[1].get("CNPJ OPERAÇÃO")
                         ,m[1].get("NOME OPERAÇÃO"))

    lst_motoristas.append(motorista)

for mot in lst_motoristas:
    print(mot)