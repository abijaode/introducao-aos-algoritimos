# Escreva um programa que leia um número inteiro positivo n e calcule a soma:

# S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... 
# usando os n primeiros termos da sequência.

# Este exercício é mais desafiador porque exige, além da repetição com while,
# o uso de uma estratégia para alternar o sinal de cada termo da soma.


numero = int(input("Digite o número: "))
resultado = 0
contador = 1
i = True

while contador <= numero:
    if i == True:
        resultado = resultado + (1 / contador)
        i = False
    else:
        resultado = resultado - (1 / contador)
        i = True
    
    contador = contador + 1

print(f"O resultado para o numero {numero} é {resultado}")
     
     