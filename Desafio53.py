f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = j[::-1]

'''for l in range(len(j) -1, -1, -1):
    i += j[l]'''
print("O inverso de {} é {}".format(j, i))
if i == j:
    print('A palvra é um palindromo')
else:
    print("A palavra não é um palindormo")
  