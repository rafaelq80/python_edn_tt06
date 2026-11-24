# Exercício 3 - Soma até zero

soma = 0
quantidade = 0

while True:
    texto = input("Digite um número inteiro (0 para encerrar): ")
    digitos = texto[1:] if texto.startswith("-") else texto
    if not digitos.isdigit():
        print("Entrada inválida. Digite um número inteiro.")
        continue
    numero = int(texto)
    if numero == 0:
        break
    soma += numero
    quantidade += 1

print(f"Soma total: {soma}")
print(f"Quantidade de números digitados: {quantidade}")
