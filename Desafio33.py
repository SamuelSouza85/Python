a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

menor = a
maior = b

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
else:
    menor = a

if a>b and a>c:
    maior = a
if c>b and c>a:
    maior = c
else:
    maior = b

print("O menor número é: {}".format(menor))
print("O maior número é: {}".format(maior))