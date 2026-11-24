
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Parabéns! Você foi Aprovado!")
elif media >= 5:
    print("Você está de Exame!")
else:
    print("Infelizmente você foi Reprovado!")