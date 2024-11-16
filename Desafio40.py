n1 = float(input('Digite a primeria nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2

if m < 5:
    print("Gostou tanto de estudar que vai refazer o ano, REPROVADO")
elif m <= 6.9:
    print("Gostou bastante de estudar que vai ficar nas férias estudando, RECUPERAÇÂO")
else:
    print("PARABENS VOCÊ FOI APROVADO")