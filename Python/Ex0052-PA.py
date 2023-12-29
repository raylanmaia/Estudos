primeiro_termo = int(input("Determine o primeiro termo: "))
razão = int(input("Determina a razão: "))
for i in range(primeiro_termo, 10*razão, razão):
    print(i)