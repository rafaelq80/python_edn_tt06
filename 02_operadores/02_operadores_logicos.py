# ou = or
# e = and
# nao = not

gosta_de_cafe = True
nao_gosta_de_cafe = not gosta_de_cafe
print(nao_gosta_de_cafe)

print("==========================================")

backend_gosta_de_cafe = True
frontend_gosta_de_chocolate = False
resultado = backend_gosta_de_cafe and frontend_gosta_de_chocolate
print(f"Conjunção (E): {resultado}")

print("==========================================")

resultado = backend_gosta_de_cafe or frontend_gosta_de_chocolate
print(f"Disjunção (OU): {resultado}")