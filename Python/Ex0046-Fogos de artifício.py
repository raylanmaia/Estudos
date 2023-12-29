from time import sleep
print("Vai começar a queima de fogos em 10 segundos, vamos começar a contagem!!")
sleep(3)
for i in range(10, 0, -1):
    print("Faltam {} segundos".format(i))
    sleep(1)
print("")
print("Feliz ano novo!!")
