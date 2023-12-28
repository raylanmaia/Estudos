peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso / altura**2
if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc <= 18.5:
    print("Você está no peso ideal!")
elif imc >= 25:
    print("Você está com sobrepeso!")
elif imc >= 30:
    print("Você está obeso!")
else:
    print("Você é obeso mórbido!")
