n = int(input("Digite um numero:"))

escolha= int(input("Clique um 1 para converte o número em binario, 2 para octal e 3 para hexadecimal:"))

if escolha == 1:
    b = bin(n)
    print("O seu número convertido em binário é {}".format(b))
elif escolha == 2:
   o = oct(n) 
   print("O seu número convertido em octal é {}".format(o))
elif escolha == 3:
    h = hex(n)
    print("O seu número convertido em hexadecimal é {}".format(h))
else:
    print("Escolha umas das opções que foram dadas")
