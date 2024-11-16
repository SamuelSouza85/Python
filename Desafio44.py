p = float(input("Qual é o preço do produto:"))
print("Dependendo da sua forma de pagamento você irá ganhar um desconto ou será cobrado juros. Pagar a vista no dinheiro você ganhará um desconto de 10%, á vista no cartão um desconto de 5%, parcelar do cartão em até 2x o preço será o mesmo, mas se você quiser parcelar em 3x ou mais será cobrado um juros de 20%.")

fp = int(input("Qual será sua forma de pagamento, digite 1 para pagar á vista no dinheiro, 2 para pagar á vista no cartâo, 3 para pagar parcelado no cartão em até 2x ou 4 para pagar parcelado em 3x ou mais no cartão: "))

if fp == 1:
    dd = p - 10/100 * p
    print("Você terá um desconto de 10% o preço final será de R${}".format(dd))
elif fp == 2:
    dc = p - 5/100 * p
    print("Você terá um desconto de 5% o preço final será de R${}".format(dc))
elif fp == 3:
    vp = p/2
    print("O valor do produto foi de R${} e cada parcela será de R${}".format(p, vp))
elif fp == 4:
    np = int(input("Em quantas parcelas você pagará:"))
    j = p + 20/100 * p
    pj = j/np
    print("O valor do produto com juros será de R${} e cada parcela sairá pelo valor de R${}".format(j, pj))
else:
    print("Escolha uma das opções dadas")