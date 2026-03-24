# Implemente um programa que leia do teclado um valor numérico N (do
# tipo inteiro positivo) e no final imprima todos os valores inteiros que compreendem
# o intervalo de 0 a N.


numero = int(input("Digite o número: "))

while numero <= 0:

    numero = int(input("Digite somente números inteiros maiores que 0!"))

sequencia = 0

while sequencia <= numero:

    print(sequencia)
    sequencia = sequencia + 1


