# Exercício 2 - Senha com tentativas

SENHA_CORRETA = "python123"
MAX_TENTATIVAS = 3

tentativas = 0
acertou = False

while tentativas < MAX_TENTATIVAS and not acertou:
    senha = input("Digite a senha: ")
    tentativas += 1
    if senha == SENHA_CORRETA:
        acertou = True
    else:
        print("Senha incorreta.")

if acertou:
    print("Acesso permitido")
else:
    print("Bloqueado")
