def main():
    path = "archives/mbox-short.txt"
    arquivo = open(path)
    
    for linha in arquivo:
        linha = linha.rstrip()
        if not linha.startswith("From"):
            continue
        
        palavra = linha.split();
        print(palavra[1])

main()