# Uma máquina industrial possui um sensor que registra sua temperatura ao longo da operação. 
# Para analisar o funcionamento do equipamento, um técnico deseja criar um programa que permita inserir várias temperaturas registradas durante o dia.
# O programa deve ler temperaturas em graus Celsius, 
# uma por vez, até que o usuário digite o valor -1, que indica o fim da coleta.
# Ao final, o programa deve informar:
# quantas temperaturas foram registradas
# a maior temperatura
# a menor temperatura
# a média das temperaturas
# quantas temperaturas estavam acima de 80 graus
# O valor -1 é apenas o marcador de encerramento e não deve ser considerado nos cálculos.


temperatura = int(input("Digite a temperatura: "))
contador = 1
maior = temperatura
menor = temperatura
maior80 = 0
total = 0
media = 0
while temperatura != -1:
    total = temperatura + total
    contador = contador + 1
    if temperatura > maior:
        maior = temperatura
    elif temperatura < menor:
        menor = temperatura
    if temperatura > 80:
        maior80 = maior80 + 1
    print("Caso queira finalizar digite (-1)")
    temperatura = int(input("Digite um novo valor: "))

media = total / contador

print(f"Foram registradas {contador} temperaturas")
print(f"A maior temperatura registrada foi: ", maior)
print(f"A menor temperatura registrada foi: ", menor)
print(f"A média de temperaturas foi: ", media)
print(f"{maior80} temperaturas foram maiores que 80 graus.")



    





