# Exercício 12 - Verificador de número primo (desafio)

def eh_primo(n):
    if n < 2:
        return False
    divisor = 2
    # Basta testar divisores até a raiz quadrada de n
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


primos = []
for numero in range(1, 101):
    if eh_primo(numero):
        primos.append(numero)

print(primos)
