# Exercício 11 - Sequência de Fibonacci (desafio)

texto = input("Quantos termos deseja ver? ")
while not texto.isdigit() or int(texto) < 1:
    texto = input("Valor inválido. Digite um inteiro positivo: ")
quantidade = int(texto)

anterior = 0
atual = 1
termos = []
for i in range(quantidade):
    termos.append(str(anterior))
    # O novo "anterior" é o "atual"; o novo "atual" é a soma dos dois
    anterior, atual = atual, anterior + atual

print(", ".join(termos))
