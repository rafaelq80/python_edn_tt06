from decimal import Decimal

# Definição de variáveis
codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario = Decimal(input("Digite o salário do funcionário: "))
vendedor = input("É vendedor? ").strip().lower()
valor = vendedor == "true"
vendedor = valor

# Checagem de tipos
print(f"Tipo da variável codigo: {type(codigo)}")
print(f"Tipo da variável nome: {type(nome)}")
print(f"Tipo da variável salario: {type(salario)}")
print(f"Tipo da variável vendedor: {type(vendedor)}")

# Exibição dos valores na tela
print(f"\nCódigo: {codigo}")
print(f"Nome: {nome}")
print(f"Salário: {salario:.2f}")
print(f"Vendedor? {vendedor}")