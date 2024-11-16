from datetime import datetime

aa = datetime.now().year
an = int(input("Qual é seu ano de nascimento: "))
i = aa - an

if i < 18:
    fi = 18 - i 
    print("Você ira se alistar futuramente, faltam {} anos".format(fi))

elif i == 18:
    print("Já é hora de se alistar")
else:
    ji = i - 18
    print("Já passou da hora de você se alistar, já se passaram {} anos do prazo".format(ji))