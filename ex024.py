nome = input("Digite o nome de uma cidade. ").strip().split()[0].title()

if nome == "Santo":
    print("O nome da cidade começa com Santo.")
else:
    print("O nome da cidade não começa com Santo.")
