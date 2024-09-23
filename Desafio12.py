vp = float(input('Qual é o preço do produto? '))
d = 5/100 * vp
nv = vp - d


print("O valor descontado é de R${:.2f}, então seu valor final fica R${:.2f}".format(d, nv))