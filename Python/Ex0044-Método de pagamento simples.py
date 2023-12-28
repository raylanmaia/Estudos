preço_produto = float(input("Qual o preço do produto? "))
pagamento = int(
    input(
        """
[1] - à vista/cheque - 10% de desconto
[2] - à vista no cartão - 5% de desconto
[3] - parcelar no cartão
Qual o método o método de pagamento: """
    )
)
if pagamento == 1:
    print(
        "O produto de preço {} reais, com desconto aplicado fica {} reais.".format(
            preço_produto, preço_produto * 90 / 100
        )
    )
elif pagamento == 2:
    print(
        "O produto de preço {} reais, com desconto aplicado fica {} reais.".format(
            preço_produto, preço_produto * 95 / 100
        )
    )
elif pagamento == 3:
    parcelas = int(input("Em quantas parcelas você quer parcelar? "))
    print(
        "O produto de preço {} reais, com a quantidade de parcelas escolhidas, fica {} parcelas de {} reais.".format(
            preço_produto, parcelas, preço_produto / parcelas
        )
    )
