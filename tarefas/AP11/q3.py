# Crie um programa em Python que leia uma matriz de 3 linhas e 4 colunas contendo números inteiros.

# O programa deve calcular e exibir a soma de todos os valores da matriz.

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
# Saída esperada
# Soma total: 78
# Observação: percorrer todos os elementos da matriz e acumular valores em uma variável.

soma = 0
matriz = []
for i in range (3):
    lista = []
    for j in range(4):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
print(matriz)
for i in range (3):
    for j in range (4):
        soma = soma + matriz[i][j]
print(soma)