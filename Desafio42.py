r1 = float(input("Informe o comprimento da primeira reta:"))
r2 = float(input("Informe o comprimento da segunda reta:"))
r3 = float(input("Informe o comprimento da terceira reta:"))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Sim é possivel se criar em triânugulo")
    if r1 == r2 == r3:
        print("Ele é um triâgunlo equilátero")
    elif r1 != r2 != r3 != r1:
        print("Ele é um triâgunlo escaleno")
    else:
        print("Ele é um triâgunlo Isósceles")
else:
    print("Não é possivel criar um triânugulo")