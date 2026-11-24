# Definindo uma lista de inteiros
numeros = [1, 2, 3, 4, 5]

# Definindo uma lista de strings
caes = ["Boxer", "Pastor Alemão", "Kangal", "Bordercollie", "Caramelo", "Pinscher", "Corgi"]

# Definindo uma lista mista
lista_mista = ["Labrador", 2, True, 2.4]

# Definido uma lista vazia
nomes = []

# Listar os elementos usando o for in
for numero in numeros:
    print(numero)

# Listar os elementos usando o for in e o enumerate
# Enumerate cria uma contagem dos elementos (iniciando em 0)
for indice, cao in enumerate(caes):
    print(f"{indice} - {cao}")

# Listar os elementos usando o for in e o enumrate
# definindo o número inicial da contagem (iniciando no parâmetro start)
for indice, elemento in enumerate(lista_mista, start=1):
    print(f"{indice} - {elemento}")
    
# Listar os elementos usando o for in e o range
# Mais próximo do for tradicional
# A função len() para encontrar o tamanho da lista
for indice in range(len(caes)):
    print(f"caes[{indice}] = {caes[indice]}")
    

# Inserir dados na lista nomes
for indice in range(5):
    nome = input(f"Digite o nome {indice + 1}: ")
    nomes.append(nome)

print(nomes)

nomes.remove("Henrique")
print(nomes)

nomes.pop(1)
print(nomes)

# nomes.clear()

print(f"Quantas vezes a Sandra aparece na lista? {nomes.count("Sandra")}")
print(f"O nome Sandra existe na lista? {nomes.index("Sandra")}")

# Ordenação Crescente
nomes.sort()
print(nomes)

# Ordenação Descrescente
nomes.sort(reverse=True)
print(nomes)

