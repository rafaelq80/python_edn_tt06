# Idade entre 18 e 69 anos
# Pessoas com idade entre 60 e 69 anos não podem doar se for a primeira vez

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

primeira_doacao = input("É a primeira doação? ").strip().lower()
valor = primeira_doacao == "true"
primeira_doacao = valor

if idade >= 60 and idade <= 69:
    if primeira_doacao:
        print(f"{nome} não está apto(a) para doar sangue!")
    else:
        print(f"{nome} está apto(a) para doar sangue!")
elif idade < 18 or idade > 69:
    print(f"{nome} não está apto(a) para doar sangue!")
else:
    print(f"{nome} está apto(a) para doar sangue!")

    