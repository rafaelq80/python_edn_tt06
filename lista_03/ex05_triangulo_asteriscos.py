# Exercício 5 - Triângulo de asteriscos

texto = input("Quantas linhas? ")
while not texto.isdigit() or int(texto) < 1:
    texto = input("Valor inválido. Digite um inteiro positivo: ")
n = int(texto)

for linha in range(1, n + 1):
    for coluna in range(linha):
        print("*", end="")
    print()
