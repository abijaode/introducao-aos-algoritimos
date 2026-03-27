# Leia dois valores inteiros: número de linhas e número de colunas. Depois, desenhe um retângulo usando o caractere *.
# Exemplo para 3 linhas e 5 colunas:
# *****
# *****
# *****
# Este exercício deve ser resolvido com repetição aninhada usando while.

coluna = int(input("Digite a quantidade de colunas: "))
linhas = int(input("Digite a quantidade de linhas: "))
quantidadel = 1
quantidadec = 1

while quantidadel <= linhas:
    quantidadel = quantidadel + 1
    quantidadec = 1
    while quantidadec <= coluna:
        print("*", end="")
        quantidadec = quantidadec + 1    
    print()