# Escreva um programa que mostre todas as tabuadas de multiplicação de 1 a 9.
# Exemplo de estrutura esperada:
# Tabuada do 1
# 1 x 1 = 1
# ...
# 1 x 10 = 10
# Tabuada do 2
# 2 x 1 = 2
# ...

numero = 0

contador = 1

resultado = 0

while numero <= 9:
    numero = numero + 1
    print("------------------")
    contador = 1
    while contador <= 9:
        resultado = numero * contador
        contador = contador + 1
        print(f"{numero} x {contador} = {resultado}")
