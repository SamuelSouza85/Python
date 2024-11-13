import calendar

ano = int(input("Qual é seu ano desejado? "))

if calendar.isleap(ano):
    print("{} é um ano bissexto".format(ano))
else:
    print("{} não é um ano bissexto".format(ano))     