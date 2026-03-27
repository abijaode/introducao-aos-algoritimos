# Um material radioativo perde metade de sua massa a cada 50 segundos. 
# Dada a massa inicial em gramas, escreva um programa 
# que determine quanto tempo será necessário para que a massa fique menor que 0,5 grama.

# Ao final, mostre:

# a massa inicial
# a massa final obtida
# o tempo total decorrido

material = float(input("Digite a massa do material: "))

massa = material
tempo = 0

while material > 0.5:
    material = material / 2
    tempo = tempo + 50

minutos = tempo / 60

print("A massa inicial foi: ", massa)
print("A massa final é : ", material)
print("O tempo decorrido em minutos foi: ", minutos)