# Escreva um programa que leia 10 números inteiros.
# Ao final, o programa deve mostrar:
# quantos números eram pares
# quantos números eram ímpares



pares = 0
impares = 0

contador = 1

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))
    
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    contador = contador + 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)