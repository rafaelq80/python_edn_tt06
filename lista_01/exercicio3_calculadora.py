num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n===== RESULTADOS =====")
print(f"Soma:          {num1} + {num2} = {num1 + num2}")
print(f"Subtração:     {num1} - {num2} = {num1 - num2}")
print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")

if num2 == 0:
    print("Divisão:       não é possível dividir por zero!")
else:
    print(f"Divisão:       {num1} / {num2} = {num1 / num2}")
print("======================")
