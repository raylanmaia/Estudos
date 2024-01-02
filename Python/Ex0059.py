from random import randint
n_pc = randint(1,10)
print(n_pc)
x = int(input("Qual número o computador pensou? "))
while x != n_pc:
    x = int(input("Você não acertou, tente novamente. "))
    if x < n_pc:
        print("O número que digitou é menor do que o computador pensou...")
    if x > n_pc:
        print("O número que digitou é maior do que o computador pensou...")
    if x == n_pc:
        print("Você acertou!")
