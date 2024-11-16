i = int(input("Qual é a sua idade: "))

if i <= 9:
    print("Você está na categoria mirim")
elif i <= 14:
    print("Você está na categoria infatil")
elif i <= 19:
    print("Você está na categoria junior")
elif i <= 20:
    print("Você está na categoria sênior")
else:
    print("Você está na categoria master")