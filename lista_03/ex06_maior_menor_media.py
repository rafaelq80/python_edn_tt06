# Exercício 6 - Maior, menor e média

numeros = []

for i in range(10):
    while True:
        texto = input(f"Digite o {i + 1}º número inteiro: ")
        digitos = texto[1:] if texto.startswith("-") else texto
        if digitos.isdigit():
            break
        print("Entrada inválida. Digite um número inteiro.")
    numeros.append(int(texto))

maior = numeros[0]
menor = numeros[0]
soma = 0

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero

media = soma / len(numeros)

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média: {media:.2f}")
print(f"Lista ordenada: {sorted(numeros)}")
