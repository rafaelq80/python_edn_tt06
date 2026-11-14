import math

print("#### CALCULADORA SIMPLES ####")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print(f"{numero1} + {numero2} = {numero1 + numero2:.2f}")
print(f"{numero1} - {numero2} = {numero1 - numero2:.2f}")
print(f"{numero1} * {numero2} = {numero1 * numero2:.2f}")
print(f"{numero1} ÷ {numero2} = {numero1 / numero2:.2f}")
print(f"{numero1} ^ {numero2} = {numero1 ** numero2:.2f}")
print(f"√{numero1} = {math.sqrt(numero1):.2f}") # Raiz Quadrada
print(f"√{numero2} = {math.sqrt(numero2):.2f}")
print(f"√{numero1} = {math.cbrt(numero1):.2f}") # Raiz Cúbica

