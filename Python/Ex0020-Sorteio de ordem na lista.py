import random
p1 = str(input("Digite o primeiro nome:"))
p2 = str(input("Digite o segundo nome:"))
p3 = str(input("Digite o terceiro nome:"))
p4 = str(input("Digite o quarto nome:"))
p5 = str(input("Digite o quinto nome:"))
sorteio = [p1, p2, p3, p4, p5]
random.shuffle(sorteio)
escolher = random.choice(sorteio)

print("A ordem dos escolhidos é {}".format(sorteio))