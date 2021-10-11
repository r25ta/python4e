import random

def main():
    #função busca um número aleatório entre 0 e 1.0 (exceto 1.0)
    print("random.random()",random.random())
    #função busca número aleatório entre 5 e 10
    print("random.randint(5,10)",random.randint(5,10)) 
    #escolher um elemento aleatório em uma sequencia
    t = [1,2,3,4,5,6,7,8,9,10]
    print("random.choice()",random.choice(t))
           
main()
print(main)
print(type(main))