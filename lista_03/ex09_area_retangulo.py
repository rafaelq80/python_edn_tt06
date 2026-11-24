# Exercício 9 - Área do retângulo

def ler_inteiro_positivo(mensagem):
    texto = input(mensagem)
    while not texto.isdigit() or int(texto) < 1:
        texto = input("Valor inválido. " + mensagem)
    return int(texto)


def area_retangulo(base, altura):
    return base * altura


base = ler_inteiro_positivo("Digite a base: ")
altura = ler_inteiro_positivo("Digite a altura: ")

print(f"A área do retângulo é {area_retangulo(base, altura)}.")
