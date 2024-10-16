l = float(input('Quantos metros de largura tem a sua parede? '))
a = float(input('Quantos metros de altura tem a sua parede? '))
A = a * l
lt = A * 2

print('A sua parede tem {}m² e será necessário {}L de tinta para pintar ela '.format(A, lt))