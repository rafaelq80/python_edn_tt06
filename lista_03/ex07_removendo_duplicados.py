# Exercício 7 - Removendo duplicados

original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sem_repeticao = []

for valor in original:
    if valor not in sem_repeticao:
        sem_repeticao.append(valor)

print(sem_repeticao)
