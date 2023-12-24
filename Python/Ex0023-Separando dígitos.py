x = int(input('Digite o número:'))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print ("A unidade é {}".format(u))
print ("A dezena é {}".format(d))
print ("A centena é {}".format(c))
print ("A milhar é {}".format(m)) 