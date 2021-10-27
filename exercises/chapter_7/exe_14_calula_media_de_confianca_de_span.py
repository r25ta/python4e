def main():
    dir = "archives/"
    arq_name=""
    try:
        arq_name = input("Digite o nome do arquivo >>")
        arq = open(dir+arq_name)
    except:
        print("Arquivo %s não encontrado" % (arq_name))

    count = 1
    note_confidence=0
    for line in arq:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            note_confidence += float(line[20:])
            count +=1
            
    media_confidence = note_confidence/count
    print("Média de confiança de span: %g" %(media_confidence))
    
main()