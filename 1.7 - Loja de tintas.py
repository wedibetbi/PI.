import math

area = float(input(""))
latas = math.ceil(area / 12 / 18)
preco = 80 * latas

print("Para uma parede de área "+"{:.2f}".format(area)+", você vai precisar de "+str(latas)+" latas, com o custo de R$ "+"{:.2f}".format(preco)+".")
