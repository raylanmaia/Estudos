import math
oposto = float(input("Digite o tamanho do cateto oposto:"))
adjacente = float(input("Digite o tamanho do cateto adjacente:"))
hipotenusa = oposto**2 + adjacente**2
hipotenusa_2 = math.sqrt(hipotenusa)

print("O valor da hipotenusa é:",hipotenusa_2)