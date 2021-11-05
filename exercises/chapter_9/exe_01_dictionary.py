def main():
    palavra = "paralelepipedo"
    d = dict()
    for p in palavra:
        if p not in d:
            d[p]=1
        else:
            d[p] +=1
    print(d)
    
main()

#if __name__=="__main__":
