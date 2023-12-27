idade = int(input("Digite sua idade para saber qual sua categoria: "))
if idade <= 9:
    print("Você é MIRIM!")
elif idade <= 14:
    print("Você é INFANTIL!")
elif idade <= 19:
    print("Você é JUNIOR!")
elif idade <= 25:
    print("Você é SENIOR!")
elif idade > 25:
    print("Você é MASTER!")
