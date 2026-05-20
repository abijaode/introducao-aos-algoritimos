# Crie um programa em Python que leia uma matriz de 3 linhas e 3 colunas contendo números inteiros.

# Depois, o programa deve exibir cada elemento acompanhado de sua posição na matriz.

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
# matriz[0][0] = 1
# matriz[0][1] = 2
# matriz[0][2] = 3
# matriz[1][0] = 4
# matriz[1][1] = 5
# matriz[1][2] = 6
# matriz[2][0] = 7
# matriz[2][1] = 8
# matriz[2][2] = 9
# Observação: praticar o acesso aos elementos usando dois índices: um para a linha e outro para a coluna.



matriz = []
for i in range (3):
    lista = []
    for j in range(3):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
print(matriz)

for i in range (3):
    for j in range (3):
        print(f"matriz [{i}] [{j}] = {matriz [i][j]}")
