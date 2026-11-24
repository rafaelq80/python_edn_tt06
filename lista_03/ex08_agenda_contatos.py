# Exercício 8 - Agenda de contatos
# Observação: a verificação com nome in agenda evita o erro de chave inexistente, dispensando o uso de exceções.

agenda = {}

while True:
    print("\n--- AGENDA ---")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Listar todos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        agenda[nome] = telefone
        print("Contato salvo.")
    elif opcao == "2":
        nome = input("Nome a buscar: ").strip()
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Nome a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print("Contato removido.")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        if len(agenda) == 0:
            print("A agenda está vazia.")
        else:
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
