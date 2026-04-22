# Crie uma função chamada calcular_valor_final(valor_produto, desconto) que receba:

# o valor original de um produto;
# o percentual de desconto concedido ao cliente.
# A função deve retornar o valor final do produto após a aplicação do desconto.

# No programa principal:

# leia o valor do produto;
# leia o percentual de desconto;
# exiba o valor final calculado.


def calcular_valor_final(valor_produto, desconto):
    resultado = valor_produto * (1 - desconto / 100)
    return resultado

valor_produto = float(input("Insira o valor do produto: "))
percentual_desconto = float(input("Digite a porcentagem de desconto: "))

preco_final = calcular_valor_final(valor_produto, percentual_desconto)

print("O preço com desconto é: ", preco_final)