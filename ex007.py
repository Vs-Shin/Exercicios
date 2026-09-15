N1 = float(input("Digite a primeira nota do aluno. "))
N2 = float(input("Digite a segunda nota do aluno. "))
M = (N1+N2)/2
print(f"A média do aluno é {M}.", end=" ")

if(M>=6):
    print("O aluno foi aprovado. ")
else:
    print("O aluno foi reprovado. ")
