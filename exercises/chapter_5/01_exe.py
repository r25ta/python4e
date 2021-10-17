
amigos = ['José', 'Maria', 'Olívia', 'Diego', 'Camila']

for amigo in amigos:
    print("Feliz Ano Novo",amigo)
    
print("Feito!")

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    
    if line == "done":
        break
    
    print(line)
print("Done!")

