# Implemente um programa que leia um valor numérico N e calcule o
# somatório:
# S = 1 + 2 + 3 + … + N
# No final, imprima o resultado do somatório


numero = int(input("Digite seu número: "))
soma = 0
sequencia = 1

while sequencia <= numero:
    print(sequencia)
    soma = soma + sequencia
    sequencia = sequencia + 1 



print("A soma da sequencia é: ", soma)