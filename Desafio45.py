from random import randint

ec = randint(1, 3)
ej = int(input("Ei vamos jogar jokenpô com certeza vou ganhar, escolha entre pedra, papel e tesoura, 1 é pedra, 2 é papel e 3 é tesoura:"))


if ec == 1:
    print("Eu escolhi pedra")
    if ej == 1:
        print("Deu empate vamos jogar denovo")
    elif ej == 2:
        print("Não acredito que perdi, foi apenas sorte de principiante vamos jogar denovo, que desta vez eu irei ganhar")
    elif ej == 3:
        print("Você é muito ruim, falei que eu ia ganhar")
    else:
        ("Não é pra roubar escolhe um dos 3")
elif ec == 2:
    print("Eu escolhi papel")
    if ej == 2:
        print("Deu empate vamos jogar denovo")
    elif ej == 3:
        print("Eu deixei você ganhar só pra vc não ficar tristinho")
    elif ej == 1:
        print("Não te culpo de ter perdido é que eu sou muito bom")
    else:
        print("Não é pra roubar escolhe um dos 3")
elif ec == 3:
    print("Eu escolhi tesoura")
    if ej == 3:
        print("Deu empate vamos jogar denovo")
    elif ej == 1:
        print("Você tem muita sorte, vamos denovo que eu irei ganhar")
    elif ej == 2:
        print("Nem em 1000 mil anos com você treinando ganharia de mim, só lendo a minha mente")
    else:
        print("Não é pra roubar escolhe um dos 3")

else:
    ("Vamos denovo")