import math

co = float(input("Digite o valor do seu cateto oposto:"))
ca = float(input("Digite o valor do seu cateto adjacente:"))
h = math.hypot(ca, co)

print("A hipotenusa de {} e {} é {:.3f}".format(co, ca, h))