l1 = int(input("Digite o primeiro lado do triângulo:"))
l2 = int(input("Digite o segundo lado do triângulo:"))
l3 = int(input("Digite o terceiro lado do triângulo:"))

if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print ("Pode formar um triângulo!")
else:
    print ("Não pode formar um triângulo")