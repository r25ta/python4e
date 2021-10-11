def calculo_pagamento(horas,taxaHora):
    txExtra = 1.5
    
    if(horas<=40):
        return horas * taxaHora
    else:
        hrsExtras = horas - 40
        vlrRegular = 40 * taxaHora
        return  vlrRegular + (hrsExtras * (taxaHora*txExtra))

def main():
    try:
        print("Sistema para calculo de horas trabalhadas")
        print("Acima de 40 hrs trabalhadas, add 1.5 no valor hora")
        strHrs = input("Digite as horas trabalhadas:")
        strTx = input("Digite o valor da taxa:") 
    
        intHrs = int(strHrs)
        floatTx = float(strTx)
    
        vlr = calculo_pagamento(intHrs,floatTx)   
        print("Pagamento:",vlr)
        
    except:
        print("Erro, por favor utilize uma entrada numérica!")
main()