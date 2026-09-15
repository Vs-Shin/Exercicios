Km = float( input("Quantos kilômetros o carro percorreu? "))
D = int( input("Por quantos dias o carro foi alugado? "))
P = (D*60) + (Km*0.15)
print ("O valor dotal é R${:.2f}.".format(P))
