import random 

c = random.randint(0, 5)

print('=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ')
print('=' * 20)

p = input("Me diga o número se vc é bom mesmo: ")

if p == c:
    print("Boa você acertou")
else:
    print("Você errou tente novamente, mas o número era {}".format(c))