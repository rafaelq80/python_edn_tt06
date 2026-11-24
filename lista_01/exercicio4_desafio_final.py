nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

maior_de_idade = idade >= 18
aprovado = media >= 7

# Par ou ímpar: usa a parte inteira da média
if int(media) % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print("\n===== BOLETIM =====")
print(f"Aluno:          {nome}")
print(f"Idade:          {idade} anos")
print(f"Notas:          {nota1}, {nota2}, {nota3}")
print(f"Média:          {media:.2f}")
print(f"Maior de idade: {'Sim' if maior_de_idade else 'Não'}")
print(f"Média (inteira) é: {paridade}")
print(f"Situação:       {'Aprovado' if aprovado else 'Reprovado'}")
print("===================")
