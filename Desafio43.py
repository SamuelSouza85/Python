p = float(input('Quantos Kg você pesa:'))
a = float(input('Qual é sua a altura:'))
imc = p / a**2

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <=25:
    print('Você está no peso ideal')
elif imc <=30:
    print('Você está em sobrecarga')
elif imc <= 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')