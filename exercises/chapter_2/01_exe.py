def pagamento_horas(horas,tx):
    txExtra = 1.5
    
    if(horas<=40):
        return horas * tx
    else:
        hrsExtras = horas - 40
        vlrRegular = 40 * tx
        return  vlrRegular + (hrsExtras * (tx*txExtra))

def main():
    print("Sistema para calculo de horas trabalhadas")
    print("Acima de 40 hrs trabalhadas, add 1.5 no valor hora")
    strHrs = input("Digite as horas trabalhadas:")
    strTx = input("Digite o valor da taxa:") 
    
    intHrs = int(strHrs)
    floatTx = float(strTx)
    
    vlr = pagamento_horas(intHrs,floatTx)   
    print("Pagamento:",vlr)
main()