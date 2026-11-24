
continua = "s"
total_respostas = 0
soma_idades = 0
futebol = 0
volei_M18 = 0

while continua.lower() != "n":

    print("***************************************")
    print("**** Pesquisa - Esportes Favoritos ****")
    print("***************************************")

    idade = int(input("Digite a sua idade: "))

    while True:
        print("Escolha o seu Esporte favorito:")
        print("1 - Futebol")
        print("2 - Voleibol")
        print("3 - Basquetebol")
        print("4 - Outros")

        esporte = int(input())

        if 1 <= esporte <= 4:
            break

    # Estatísticas
    total_respostas += 1
    soma_idades += idade

    if esporte == 1:
        futebol += 1 

    if idade > 18 and esporte == 2:
        volei_M18 +=1

    continua = input("Deseja Continuar? (S/N): ").strip().lower()

print(f"Total de pessoas que gostam de futebol: {futebol}")
print(f"Total de pessoas maiores de 18 anos que gostam de vôleibol: {volei_M18}")
print(f"Total de pessoas responderam a pesquisa: {total_respostas}")
print(f"Média de idade das pessoas que responderam a pesquisa: {soma_idades / total_respostas:.2f}")
