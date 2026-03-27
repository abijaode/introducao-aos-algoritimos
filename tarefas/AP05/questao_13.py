# Leia um número inteiro positivo n e mostre um triângulo de números.
# Para n = 5, a saída deve ser:
# 1
# 12
# 123
# 1234
# 12345


numero = int(input("Digite o numero: "))

contador = 0

c = ""

while contador < numero:
    contador = contador + 1
    c = c + str(contador)
    print(str(c))

    
    

    