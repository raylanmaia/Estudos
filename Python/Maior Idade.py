p1 = int(input("Digite o ano de nascimento da primeira pessoa: "))

for i in range(p1, 2025):
    if p1 >= 18:
        print("O P1 é maior de idade e tem {}".format(2024 - p1))