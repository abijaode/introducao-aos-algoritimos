# Crie uma função chamada calcular_comissao(valor_venda) que receba o valor de uma venda
# e retorne a comissão correspondente a 5% desse valor.

# No programa principal:

# leia o valor da venda;
# chame a função;
# exiba o valor retornado.



def comissao(valor_venda):
    valor_venda = valor_venda * 0.05
    return valor_venda
valor_venda = float(input("Insira o valor da venda: "))

comissao(valor_venda)

print("A comissao é: ", comissao(valor_venda))

