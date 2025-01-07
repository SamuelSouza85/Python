p1 = int(input(("Qual é o primeiro termo da sua PA:")))
r = int(input(("Qual é a razão da sua PA:")))
pa = p1 + (10 - 1) * r

for c in range(p1, pa + r, r):
    print("{}".format(c), end=' -> ')
print("Fim")