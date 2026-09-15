from math import sin, cos, tan, radians

ângulo = float(input("Digite o ângulo que você deseja. "))
seno = sin(radians(ângulo))
print("O seno do ângulo {} é {:.2f}.".format(ângulo, seno))
cosseno = cos(radians(ângulo))
print("O cosseno {:.2f}".format(cosseno))
tangente = tan(radians(ângulo))
print("A tangente é {:.2f}.".format(tangente))
