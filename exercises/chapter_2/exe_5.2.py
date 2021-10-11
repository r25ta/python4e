def main():
    min = None
    max = None

    while True:
        s_number= input("Enter a Number ")
        
        if s_number == "done":
            break
        
        try:
            number = int(s_number)
        
        except:
            print("Invalid input")
            continue
        
        if max is None:
            max = number
        
        elif number > max:
            max = number
        
        
        if min is None:
            min = number
        
        elif number < min:
            min = number
            
    print("Maximum is",max)
    print("Minium is",min)
    
main()