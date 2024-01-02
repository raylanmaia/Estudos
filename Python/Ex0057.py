sexo = str(input("Digite seu sexo: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Digite o sexo, por favor!")).strip().upper()[0]
print("Seu sexo é {}!".format(sexo))