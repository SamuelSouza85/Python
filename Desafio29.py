v = int(input("Qual foi a velocidade do carro? "))

if v > 80:
    print("Ta achando que ta disputando corrida")
    m = (v-80) * 7
    print("Paga esse R${:.2f} de multa por ter passado a velocidade máxima".format(m))
else:
    print("Tenha um bom dia")