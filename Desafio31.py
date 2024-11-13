km = float(input("Quantos Km teram a viagem? "))

if km < 200:
    p = km * 0.50
    print("A viagem custará R${}".format(p))
else:
    p = km * 0.45
    print("A viagem custará R${}".format(p))