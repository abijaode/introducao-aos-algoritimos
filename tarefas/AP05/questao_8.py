# Escreva um programa que leia números inteiros indefinidamente, até que o usuário digite 0.
# O valor 0 deve ser usado apenas como sinal de parada e não deve ser somado.
# Ao final, o programa deve mostrar:
# a soma de todos os números informados
# a quantidade de números digitados, sem contar o zero

soma = 0

contador = 0

numero = (int(input("Digite um numero: ")))

while numero != 0:
    
    soma = numero + soma
    contador = contador + 1
    print("Caso queira finalizar a soma digite 0.")
    numero = (int(input("Digite um novo numero: ")))

print("A soma total é: ", soma)
print("A quantidade de numeros digitados é: ", contador)