vc = float(input('Qual é o valor da casa: '))
s = float(input('Qual é o valor do seu salário: '))
a = int(input('Em quantos anos você deseja pagar a casa:'))
m = a * 12
p = vc/m

if p > 30/100 * s:
    print("Seu empréstimo foi negado")
else:
    print("Seu empréstimo foi aceito")
