idade_joao = 18
idade_maria = 21
idade_pedro = 18

resultado = idade_maria > idade_joao
print(f"Maria é mais experiente do que João? {resultado}")

resultado = idade_pedro == idade_joao
print(f"Pedro tem a mesma idade que João? {resultado}")

resultado = idade_pedro != idade_joao
print(f"Pedro e João possuem idades diferentes? {resultado}")

eh_adulto = 18 <= idade_joao < 65
print(f"João é adulto (idade entre 18 e 65 anos)? {eh_adulto}")
