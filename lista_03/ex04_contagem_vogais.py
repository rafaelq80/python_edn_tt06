# Exercício 4 - Contagem de vogais
# Observação: vogais acentuadas (á, é, ã etc.) não são contadas, pois o enunciado pede apenas a, e, i, o, u.

frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase possui {contador} vogais.")
