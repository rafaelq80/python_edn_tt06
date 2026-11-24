colaborador = {
    "nome": "Ravini Villas Boas",
    "email": "ravini@edn.com.br",
    "dataNascimento": "1998-01-12",
    "salario": 10000.00,
    "cargo": "Desenvolvedora Full Stack Sênior"
}

print(colaborador)

print(f"Nome da colaboradora: {colaborador["nome"]}")

print(f"Chaves do dicionário colaborador: {colaborador.keys()}")
print(f"Valores armazenados no dicionário colaborador: {colaborador.values()}")

colaborador.pop("cargo")
print(colaborador)