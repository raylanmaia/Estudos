from time import sleep
from PIL import Image
l1 = int(input("Digite o primeiro lado do triângulo:"))
l2 = int(input("Digite o segundo lado do triângulo:"))
l3 = int(input("Digite o terceiro lado do triângulo:"))
print("=="*20)
print("Analisando o triângulo....")
print("=="*20)
sleep(2)
if l1 < l2+l3 and l2 < l3+l1 and l3 < l1+l2:
    print("É possível formar o triângulo!")
    if l1 == l2 == l3:
        print("É um triângulo equilátero!")
    elif l1 == l2 != l3:
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
