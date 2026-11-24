# Exercício 10 - Maior de dois números

def ler_inteiro(mensagem):
    texto = input(mensagem)
    digitos = texto[1:] if texto.startswith("-") else texto
    while not digitos.isdigit():
        texto = input("Valor inválido. " + mensagem)
        digitos = texto[1:] if texto.startswith("-") else texto
    return int(texto)


def maior_de_dois(a, b):
    if a > b:
        return a
    return b


x = ler_inteiro("Digite o primeiro número: ")
y = ler_inteiro("Digite o segundo número: ")

print(f"O maior número é {maior_de_dois(x, y)}.")
