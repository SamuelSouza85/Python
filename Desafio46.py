import time

pronto = str(input("Você está pronto? S/N:")).upper()


if pronto == "S":
    for c in range(0, 11):
        print(c)
        time.sleep(1)
elif pronto == "N":
    print("Tudo bem até a próxima")
else:
    print("Digite S ou N")