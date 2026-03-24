# Escreva um programa que leia 5 notas informadas pelo usuário e, ao final, calcule e mostre a média aritmética dessas notas.
# Este exercício exige o uso de repetição com contador e acumulador.

contador = 1
resultado = 0

while contador <= 5:
    nota = int(input(f"Digite a {contador} nota: "))
    resultado = resultado + nota
    contador = contador + 1

media = resultado / 5

print("A média é:", media)
