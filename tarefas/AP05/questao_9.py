# Uma pequena loja deseja registrar as vendas realizadas durante um dia. 
# Para isso, o operador do caixa informará o valor de cada venda, uma por vez. 
# O processo deve continuar até que seja digitado o valor 0, indicando que não há mais vendas a registrar.
# Escreva um programa que leia os valores das vendas e, ao final, mostre:
# o valor total vendido no dia
# a quantidade de vendas registradas
# o valor médio das vendas
# O valor 0 serve apenas para encerrar a entrada de dados e não deve ser considerado como venda.

contador = 0
media = 0
total = 0

venda = (int(input("Digite o valor da venda:")))

while venda != 0:
    contador = contador + 1
    total = total + venda
    venda = (int(input("Digite o valor do novo produto: ")))

media = total / contador

print("O valor vendido ao fim do dia é: ", total)
print("A quantidade de vendas registradas é: ", contador)
print("O valor médio das vendas foi: ", media)