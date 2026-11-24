
continua = True

while continua:

    entrada = input("Digite um numero inteiro: ")

    try:
        numero = int(entrada)
        print("É um número inteiro!")
        continua = False
    except ValueError:
        print("Não é um número inteiro! \nDigite novamente!")
