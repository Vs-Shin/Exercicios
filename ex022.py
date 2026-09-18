nome = input("Digite seu nome completo. ").strip()
print("O nome em maiúsculo é {} e em minúsculo é {}.".format(nome.upper(), nome.lower()))
print("A quantidade de caracteres, sem contar espaços, que o nome possui é: {}.".format(len(nome) - nome.count(" ")))
print("A quantidade de caracteres do primeiro nome é: {}".format(len(nome.split()[0])))
