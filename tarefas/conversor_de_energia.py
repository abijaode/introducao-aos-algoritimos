# Uma residência deseja estimar o consumo mensal de energia de um equipamento.

# Leia:

# potência do aparelho (Watts)
# horas de uso por dia
# dias de uso no mês
# preço da energia (R$/kWh)
# Após ler os dados, calcule o consumo diário, consumo mensal e custo mensal (em reais), e os imprima na tela.

# Para calcular o consumo diário, devemos calcular: (potencia * horas) / 1000
# Saída esperada:

# Relatório de consumo
# --------------------
# Consumo diário (kWh): ...
# Consumo mensal (kWh): ...
# Custo mensal (R$): ...


watts = float(input("Digite a potencia do aparelho (em Watts): "))
horas = float(input("Digite quanto tempo o aparelho fica ligado (por dia): "))
dias = float(input("Digite quantos dias por mes o apareho é utilizado: "))
preco = float(input("Digite o preço da energia (R$/kWh): "))
consumodiario = watts * horas / 1000
consumomensal = consumodiario * 30
customensal = consumomensal * preco

print("Relatório de consumo")
print("--------------------")
print(f"Consumo diário (kWh): {consumodiario}")
print(f"Consumo mensal kWh: {consumomensal}")
print(f"Custo mensal (R$): {customensal}")