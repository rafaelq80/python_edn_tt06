
tarefas = []

def cadastrar():
  tarefa = input("\nDigite a Nova Tarefa: ").strip()
  if tarefa:
    tarefas.append(tarefa)
    print("\nTarefa adicionada!")
  else:
    print("\nA Tarefa não pode ser vazia!")

def listar():
  if not tarefas:
    print("\nNão existe nenhuma Tarefa na lista!")
    return
  
  print("\n***** Tarefas *****")
  for indice, tarefa in enumerate(tarefas, start=1):
    print(f"{indice} - {tarefa}")

def atualizar():
  listar()

  if not tarefas:
    return

  indice = ler_indice("\nDigite o número da tarefa: ")

  if indice is None:
    return

  novo_texto = input("\nDigite a atualização da tarefa: ").strip()

  if novo_texto:
    tarefas[indice] = novo_texto
    print("\nTarefa Atualizada!")
  else:
    print("\nO texto da tarefa não pode ser vazio!")

def ler_indice(mensagem):
  try:
    indice = int(input(mensagem))
  except ValueError:
    print("\nDigite um número inteiro válido!")
    return None
  
  if indice < 1 or indice > len(tarefas):
    print("\nIndice inexistente")
    return None

  return indice - 1

def deletar():
  listar()

  if not tarefas:
    return

  indice = ler_indice("\nDigite o número da tarefa")

  if indice is None:
    return

  removida = tarefas.pop(indice)

  print(f"\nTarefa {removida} Deletada com sucesso!")

def menu():
  while True:
    print("\n***** TODO LIST *****")
    print("1 - Cadastrar Tarefa")
    print("2 - Listar todas as Tarefas")
    print("3 - Atualizar Tarefa")
    print("4 - Deletar Tarefa")
    print("0 - Sair")

    opcao = input("\nEscolha a opção desejada: ").strip()

    match opcao:
      case "1":
        cadastrar()
      case "2":
        listar()
      case "3":
        atualizar()
      case "4":  
        deletar()
      case "0":
        print("Até logo!")
        break
      case _:
        print("Opção inválida")

menu()