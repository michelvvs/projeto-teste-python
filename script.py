nome = input("me fale seu nome: ")
print(nome)

with open("baseDados.csv", "a") as arquivo:
    arquivo.write(f"{nome}, ")