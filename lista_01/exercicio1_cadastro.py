nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
matriculado_texto = input("Está matriculado? (True ou False): ")
matriculado = matriculado_texto.strip().lower() == "true"

print("\n===== CADASTRO DO ALUNO =====")
print(f"Nome:        {nome}")
print(f"Idade:       {idade} anos")
print(f"Matriculado: {matriculado}")
print("=============================")
