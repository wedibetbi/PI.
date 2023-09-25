import math
area = float(input(""))

l = (area / 12) #calcula a quantidade de litros de tinta necessários para cobrir a área a ser pintada
n1 = math.ceil(l / 18) #calcula a quantidade de latas de 18 litros e arredonda pra cima
n2 = math.ceil(l / 3.6) #calcula a quantidade de galões de 3.6 litros e arredonda pra cima
n3 = math.floor(l / 18) #calcula a quantidade de latas de 18 litros e arredonda pra baixo
n4 = math.ceil((l % 18) / 3.6) #calcula a quantidade de galões de 3.6 litros e arredonda pra cima

preco1 = 80 * n1 #calcula o valor a ser pago por apenas latas
preco2 = 25 * n2 #calcula o valor a ser pago por apenas galões
preco3 = (80 * n3) + (25 * n4) #calcula o valor a ser pago por latas e galões

print("Para uma parede de área "+"{:.2f}".format(area)+", você vai precisar de "+str(n1)+" latas de 18 litros, com o custo de R$ "+"{:.2f}".format(preco1)+".")
print("Para uma parede de área "+"{:.2f}".format(area)+", você vai precisar de "+str(n2)+" latas de 3,6 litros, com o custo de R$ "+"{:.2f}".format(preco2)+".")
print("Para uma parede de área "+"{:.2f}".format(area)+", você vai precisar de "+str(n3)+" latas de 18 litros e "+str(n4)+" latas de 3,6, com o custo de R$ "+"{:.2f}".format(preco3)+".")
