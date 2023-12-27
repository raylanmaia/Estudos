from time import sleep
n_1= float(input("Digite sua primeira nota: "))
n_2= float(input("Digite sua primeira nota: "))
n_3= float(input("Digite sua primeira nota: "))
média = (n_1+n_2+n_3)/3
print("Calculando suas notas!")
sleep(2)
print("Sua média é {:.2f}".format(média))
if média >= 7:
    print("Aprovado!")
elif média < 5:
    print("Reprovado!")
else:
    print("Você está de recuperação!")

