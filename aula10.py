n1 = float(input('Digite a primeria nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2

print('A média do aluno foi {:.1f}'.format(m))

if m >= 6.0:
    print("Sua média foi boa")
else:
    print("Sua média foi horrivel vai estudar")