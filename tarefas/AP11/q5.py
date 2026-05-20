# Crie um programa em Python que leia uma matriz de 3 linhas e 4 colunas.

# Depois, o programa deve calcular e exibir a soma dos valores de cada linha.

# Exemplo de entrada
# 1
# 2
# 3
# 4
# 5
# 5
# 5
# 5
# 10
# 20
# 30
# 40
# Saída esperada
# Soma da linha 0: 10
# Soma da linha 1: 20
# Soma da linha 2: 100


matriz = []
for i in range (3):
    lista = []
    for j in range(4):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
print(matriz)

for i in range(3):
    soma = 0               
    for j in range(4):
        soma = soma + matriz[i][j]  
    print(f"Soma da linha {i}: {soma}")

