# Crie um programa em Python que leia uma matriz de 3 linhas e 3 colunas.

# Depois, o programa deve calcular e exibir a soma dos valores de cada coluna.

# Exemplo de entrada
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Saída esperada
# Soma da coluna 0: 12
# Soma da coluna 1: 15
# Soma da coluna 2: 18


matriz = []
for i in range (3):
    lista = []
    for j in range(3):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
print(matriz)

for j in range(3):
    soma = 0               
    for i in range(3):
        soma = soma + matriz[i][j]  
    print(f"Soma da coluna {j}: {soma}")
