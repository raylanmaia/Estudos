preço_produto = float(input("Qual preço do produto? "))
forma_pagamento = str(input("O pagamento será à vista ou parcelado?"))
pagamento_dinheiro = preço_produto * 90/100
pagamento_cartão = preço_produto * 95/100
if forma_pagamento == "a vista" or "à vista":
    dinheiro_cartão = str(input("Dinheiro ou cartão?"))
    if dinheiro_cartão == "Dinheiro" or "dinheiro" :
            print("O valor do produto será {} reais, por conta do desconto de 10% do pagamento à vista no dinheiro ou cheque!".format(pagamento_dinheiro))
    elif dinheiro_cartão == "Cartão" or "cartão":
        cartao_a_vista_parcelado = str(input("O pagamento com o cartão será à vista ou parcelado?"))
    if cartao_a_vista_parcelado ==  "a vista" or "à vista":
        print("O valor do produto será {} reais, por conta do desconto de 5% do pagamento no cartão!".format(pagamento_cartão))
if cartao_a_vista_parcelado == "parcelado":
    parcelas = int(input("Digite a quantidade de parcelas: "))
if parcelas == 2:
    print("Você pagará duas parcelas de {} reais.".format(preço_produto / 2))
if parcelas >= 3:
    print("Você pagará {} parcelas de {} reais.".format(parcelas, preço_produto / parcelas))
