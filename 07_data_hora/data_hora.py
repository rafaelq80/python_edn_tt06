import datetime as dt

# Nomes dos meses na mesma ordem usada pelo número do mês (janeiro = 1).
meses = [
  "janeiro", 
  "fevereiro", 
  "março", 
  "abril", 
  "maio", 
  "junho",
  "julho", 
  "agosto", 
  "setembro", 
  "outubro", 
  "novembro", 
  "dezembro"
]

# A função weekday() usa índices de 0 (segunda-feira) a 6 (domingo).
dias_semana = [
  "segunda-feira", 
  "terça-feira", 
  "quarta-feira", 
  "quinta-feira",
  "sexta-feira", 
  "sábado", 
  "domingo"
]

hoje = dt.date.today()
print(f"Hoje é dia {hoje}")
print(f"Hoje é dia {hoje.strftime('%d/%m/%Y')}")

print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

data_digitada = input("Digite uma data válida (DD/MM/AAAA): ").strip()

try:
  data_convertida = dt.datetime.strptime(data_digitada, '%d/%m/%Y').date()
except ValueError:
  print("Data Inválida!")

print(f"\n Data Digitada: {data_convertida}")