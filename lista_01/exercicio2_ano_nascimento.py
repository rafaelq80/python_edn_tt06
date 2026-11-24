ANO_ATUAL = 2026

nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))

idade = ANO_ATUAL - ano_nascimento

print("\n===== RESULTADO =====")
print(f"Nome:  {nome}")
print(f"Idade: {idade} anos")
print("=====================")
