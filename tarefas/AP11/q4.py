# Crie um programa em Python que leia uma matriz de 3 linhas e 3 colunas.

# Depois, o programa deve encontrar e exibir o maior valor armazenado na matriz.

# Exemplo de entrada
# 8
# 3
# 10
# 4
# 15
# 6
# 2
# 7
# 1
# Saída esperada
# Maior valor: 15
# Observação: inicializar corretamente a variável que guarda o maior valor. 
# Uma boa estratégia é começar usando o primeiro elemento da matriz.


matriz = []
for i in range (3):
    lista = []
    for j in range(3):
        numero = int(input("Digite o numero: "))
        lista.append(numero)
    matriz.append(lista)
print(matriz)

maior = matriz[0][0]

for i in range (3):
    for j in range (3):
        if maior < matriz [i][j]:
            maior = matriz [i][j]

print(maior)
