from random import randint
computador = randint(0, 5)
e1 = int(input("Digite um número entre 0 e 5:"))
print ("processando...")
if computador == e1:
    print ('Você acertou!')
else:
    print ('Você errou, tente de novo!')