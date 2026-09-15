from math import hypot

co = float(input("Digite o comprimento do cateto oposto. "))
ca = float(input("Digite o comprimento do cateto adjacente. "))
h = hypot(co, ca)
print("O cateto da hipotenusa tem {:.2f} de diâmetro.".format(h))
