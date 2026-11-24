# Exercício 1 - Contar números pares até N

texto = input("Digite um número N: ")
while not texto.isdigit() or int(texto) < 1:
    texto = input("Valor inválido. Digite um inteiro positivo: ")
n = int(texto)

pares = 0
for numero in range(1, n + 1):
    if numero % 2 == 0:
        pares += 1

print(f"Existem {pares} números pares de 1 até {n}.")
