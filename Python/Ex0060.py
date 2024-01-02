n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opções = 0
while opções != 5:
    opções = int(
        input(
            """[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Digite a opção: """
        )
    )
    if opções == 1:
        print("O resultado de {} + {}, é {}!".format(n1, n2, n1 + n2))
    elif opções == 2:
        print("O resultado de {} * {}, é {}!".format(n1, n2, n1 * n2))
    elif opções == 3 and n1 > n2:
        print("O número {} é maior que {}.".format(n1, n2))
    elif opções == 3 and n1 == n2:
        print("O número {} é igual ao {}.".format(n1, n2))
    elif opções == 3 and n1 < n2:
        print("O número {} é menor que {}.".format(n1, n2))
    elif opções == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
