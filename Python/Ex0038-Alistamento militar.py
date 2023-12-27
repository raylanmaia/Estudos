from time import sleep
idade = int(input("Quantos anos você tem?"))
print("Analisando...")
sleep(2)
if idade  < 18:
    print("Ainda falta {} anos para você se alistar".format(18-idade))
elif idade > 18:
    print("Você já deveria ter se alistado a {} anos!".format(idade-18))
elif idade == 18:
    print("Você está na idade do alistamento!")