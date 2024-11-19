n = int(input("Qual é seu número desejado: "))

for c in range(1, 11):
    t = n * c
    print("{} x {} = {}".format(n, c, t))
