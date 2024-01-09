from time import sleep
print("Bem vindo a SUPER CALCULADORA!")
sleep(2)
opção = str(input("Quer iniciar a calculadora? S/N: \n")).strip().upper()
if opção == "S":
    while opção != 0:
        opção = int(
        input(
            "[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Sair\nDigite a opção desejada:\n"
        )
    )
        n1 = int(input("Digite o primeiro número:\n"))
        n2 = int(input("Digite o segundo número:\n"))
        if opção == 1:
            print("{} + {} = {}".format(n1, n2, n1 + n2))
        elif opção == 2:
            print("{} - {} = {}".format(n1, n2, n1 - n2))
        elif opção == 3:
            print("{} * {} = {}".format(n1, n2, n1 * n2))
        elif opção == 4:
            print("{} / {} = {}".format(n1, n2, n1 / n2))
        opção = int(input("Gostaria de continuar e fazer outra operação? 1 para SIM / 0 para NÃO:\n"))
    print("")
    print("Obrigado por usar a SUPER CALCULADORA!")
else:
    print("Obrigado por usar a calculadora")