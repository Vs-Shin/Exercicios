A = float(input("Digite a altura da parede. "))
L = float(input("Digite a largura da parede. "))
Ar = A*L
L = Ar/2
print("A area da parede é de {}M² e a quantidade de litros de tinta para pintá-la é {:.2f}.".format(Ar, L))
