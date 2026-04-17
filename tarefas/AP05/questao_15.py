# Escreva um programa que leia um número inteiro positivo n e calcule a soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# Ao final, mostre o valor de S.
# Este exercício é um primeiro passo para trabalhar séries com frações utilizando repetição com while.


numero = int(input("Digite o número: "))
soma = 0
contador = 1
resultado = 0

while contador <= numero:
    soma = 1 / contador
    resultado = resultado + soma
    contador = contador + 1

print(f"A soma do numero {numero} é {resultado}.")
