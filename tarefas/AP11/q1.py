# Crie um programa em Python que leia os valores de uma matriz de 2 linhas e 3 colunas.

# O programa deve exibir a matriz completa, linha por linha.

# Exemplo de entrada
# 1
# 2
# 3
# 4
# 5
# 6
# Saída esperada
# [1, 2, 3]
# [4, 5, 6]
# Observação: criar uma matriz como lista de listas, usar dois laços de repetição e adicionar valores com append.




matriz = []
for i in range(2):
    lista = []
    for j in range(3):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
for linha in matriz:
    print(linha)