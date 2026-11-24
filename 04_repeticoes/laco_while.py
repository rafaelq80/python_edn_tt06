
continua = "s"

while continua.lower() != "n":

    numero1 = int(input("\nDigite o primeiro número: "))
    numero2 = int(input("\nDigite o segundo número: "))

    print(f"O resultado da soma é {numero1 + numero2}")

    continua = input("Digite S para continuar ou N para sair: ")