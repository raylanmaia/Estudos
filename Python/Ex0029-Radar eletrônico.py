from time import sleep
velocidade = int(input("Qual a velocidade do condutor?")) #velocidade que o carro estava
sleep(2)
print ("Analisando a filmagem!")
sleep(2)
multa = (velocidade - 80) * 7
if velocidade > 80:
    print ("Você estava a mais de 80Km/h, você será multado.")
    print ("A multa será de {} reais!".format(multa))
else:
    print ("Você estava na velocidade normal da via!")