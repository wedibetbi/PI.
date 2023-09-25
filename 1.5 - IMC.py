peso = float(input(""))
altura = float(input(""))
imc = peso / (altura ** 2)
print("Para um peso de "+"{:.2f}".format(peso)+" e altura "+"{:.2f}".format(altura)+", o IMC calculado é "+"{:.2f}".format(imc)+".")
