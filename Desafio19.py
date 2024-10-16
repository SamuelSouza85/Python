import random

a1 = str(input("Fale o nome do primeiro aluno:"))
a2 = str(input("Fale o nome do segundo aluno:"))
a3 = str(input("Fale o nome do terceiro aluno:"))
a4 = str(input("Fale o nome do quarto aluno:"))
at = [a1, a2, a3, a4]
As = random.sample(at, 1)

print("O aluno escolhido para apagar o quadro foi o(a) {}".format(As))