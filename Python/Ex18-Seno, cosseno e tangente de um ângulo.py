import math
angulo = int(input("Digite o ângulo:"))
cos = math.cos(math.radians(angulo))
sin = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print ("O conseno é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}.".format(cos, sin, tan))