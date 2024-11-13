s = float(input("Qual é o seu salário:"))


if s>1250.00:
    ss = 10/100 * s + s
    print("O seu reajuste salarial foi de 10% o preço final foi equivalente a {}".format(ss))
else:
    si = 15/100 * s + s
    print("O seu reajuste salarial foi de 15% o preço final foi equivalente a {}".format(si))


