km = int(input("Digite a distância em KM da viagem:"))
if km <= 200:
    print("Você pagará {} reais por essa viagem!".format(km*0.5))
else:
    print("Você pagará {} reais por essa viagem!".format(km*0.45))