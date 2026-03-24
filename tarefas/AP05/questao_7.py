# Escreva um programa que leia 8 números inteiros e determine:
# o maior valor informado
# o menor valor informado
# Ao final, mostre os dois resultados.

contador = 1

numero = int(input(f"Digite o {contador} numero: "))
maior = numero
menor = numero

contador = contador + 1

while contador <= 8:
    numero = int(input(f"Digite o {contador} numero: "))
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero
    
    contador = contador + 1

print(f"O maior número é {maior} e o menor é {menor}")