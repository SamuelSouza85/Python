frase = str(input('Qual é seu Nome Completo?')).strip()
Nm = frase.upper()
nm = frase.lower()
se = frase.replace(" ", "")
pn = frase.split()


print("Seu nome em maiúsculas é {}".format(Nm))
print("Seu nome em minúsculas é {}".format(nm))
print("Seu nome ao todo {} letras".format(len(se)))
print("Seu primeiro nome é {} e ele tem {} letras".format(pn[0], len(pn[0])))