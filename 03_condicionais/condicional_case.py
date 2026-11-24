# Para funcionar precisa no minimo da versão 3.10 Python

print("### Menu ###")
print("1 - Indicação de Livro")
print("2 - Frase Motivacional")
print("3 - Indicação de Música")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print("Livro: O Alquimista")
    case 2:
        print("Frase: Se você cair, Levante!")
    case 3:
        print("Música: AURORA - No Cure For Me.")
    case _:
        print("Opção Inválida!")
