produto = ("Notebook", 3500.00, "Informática")

print(f"Produto: {produto}")

for informacao in produto:
    print(f"→ {informacao}")

print(f"Tamanho da tupla produto: {len(produto)}")

print(f"'Fatiar' a tupla e exibir os 2 primeiros elementos {produto[0:2]}")

print(produto[1])
