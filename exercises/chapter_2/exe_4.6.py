def computepay(h, r):
    pay = h * r
    xtras_hours = 0
    pay_xtras_hours = 0
    
    if h > 40:
        xtras_hours = h - 40
    
    if xtras_hours > 0:
        pay_xtras_hours = xtras_hours * (r/2)
        
    total_pay = pay + pay_xtras_hours

    return total_pay

def main():
    s_hrs = input("Enter Hours:")
    s_tx_hrs = input("Enter Rate per Hour:")
    
    try:
        f_hrs = float(s_hrs)
    except:
        print("Invalid input for Hours, please enter only values numberic")
        quit()
    try:            
        f_tx_hrs = float(s_tx_hrs)
    
    except:
        print("Invalid input for Rate per Hour, please enter only values numberic")
        quit()
                
    p = computepay(f_hrs, f_tx_hrs)
    print("Pay", p)
    
main()