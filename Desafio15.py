d = int(input('Por quantos dias o carro foi alugado?'))
q = float(input('Quantos km foram rodados com o carro?'))

vd = d * 60
vq = q * 0.15
va = vq + vd

print('O valor do aluguel do carro é de R${:.2f}'.format(va))