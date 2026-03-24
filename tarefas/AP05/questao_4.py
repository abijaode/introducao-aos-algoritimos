# Escreva um programa que leia um número inteiro e mostre a sua tabuada de 1 a 10.
# Exemplo: se o número informado for 7, o programa deve mostrar:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70


numero = (int(input("Digite seu número: ")))

contador = 1

resultado = 0

while contador <= 10:
    resultado = numero * contador
    contador = contador + 1
    numero = numero + 1
    print(resultado)

