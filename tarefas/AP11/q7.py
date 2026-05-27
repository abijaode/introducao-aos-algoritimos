# Contando pares e ímpares
# Crie um programa em Python que leia uma matriz de 4 linhas e 4 colunas contendo números inteiros.

# O programa deve contar e exibir:

# a quantidade de números pares por linha;
# a quantidade de números ímpares por coluna.
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
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# Saída esperada
# Pares: [2,2,2,2]
# Impares: [4,0,4,0]


matriz = []
for i in range(4):
    lista = []
    for j in range(4):
        numero = int(input("digite o numero: "))
        lista.append(numero)
    matriz.append(lista)

pares_por_linha = []
for i in range(4):
    contagem = 0
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            contagem += 1
    pares_por_linha.append(contagem)

impares_por_coluna = []
for j in range(4):
    contagem = 0
    for i in range(4):
        if matriz[i][j] % 2 != 0:
            contagem += 1
    impares_por_coluna.append(contagem)

print(f"Pares: {pares_por_linha}")
print(f"Impares: {impares_por_coluna}")