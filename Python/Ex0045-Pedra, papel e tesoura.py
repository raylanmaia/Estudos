import random

opções = int(
    input(
        """Suas opções são:
[1] - Pedra
[2] - Papel
[3] - Tesoura
Qual você escolhe? 
"""
    )
)
máquina = random.randint(1, 3)
print(máquina)
if máquina == opções:
    print("Empatou!")
elif máquina == 1 and opções == 3:
    print("Você perdeu!")
elif máquina == 1 and opções == 2:
    print("Você ganhou!")
elif máquina == 3 and opções == 1:
    print("Você ganhou!")
elif máquina == 2 and opções == 1:
    print("Você perdeu!")
elif máquina == 1 and opções == 3:
    print("Você perdeu!")
elif máquina == 2 and opções == 3:
    print("Você perdeu!")