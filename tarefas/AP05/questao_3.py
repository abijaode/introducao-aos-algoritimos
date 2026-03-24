# Escreva um programa que leia um número inteiro positivo n e calcule a soma dos números de 1 até n.
# Exemplo: se o usuário digitar 5, o programa deverá calcular:
# 1 + 2 + 3 + 4 + 5
# e mostrar o resultado final.

numero = int(input("Digite seu número: "))

contador = 1
soma = 0

while contador <= numero:
    soma = soma + contador
    contador = contador + 1

print("O resultado é:", soma)