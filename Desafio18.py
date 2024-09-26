import math

a = int(input("Digite o valor do seu ângulo:"))
ar = math.radians(a)
c = math.cos(ar)
s = math.sin(ar)
t = math.tan(ar)
print("O valor do seu cosseno é {:.4f} do seu seno {:.4f} e da sua tangente é {:.4f}".format(c, s, t))
