# Uma loja está desenvolvendo um pequeno sistema para registrar o fechamento de um atendimento no balcão. 
# Ao final de cada venda, o sistema deve organizar as informações principais para que o atendente 
# veja, de forma clara, quem foi atendido, quanto o cliente pagará e qual comissão será gerada pela venda.

# Para isso, escreva um programa que utilize as funções e procedimentos criados nos exercícios anteriores deste bloco.

# O programa deve:

# exibir o cabeçalho do sistema;
# ler o nome do cliente e mostrá-lo na tela;
# ler o valor original do produto;
# ler o percentual de desconto oferecido;
# calcular o valor final da compra;
# calcular a comissão do vendedor com base no valor final da venda;
# exibir um resumo do atendimento.
# Entradas:

# nome do cliente;
# valor original do produto;
# percentual de desconto.
# Saídas esperadas:

# o cabeçalho do sistema;
# a identificação do cliente;
# o valor original do produto;
# o desconto aplicado;
# o valor final da compra;
# a comissão calculada sobre o valor final.
# Importante: neste exercício, as funções anteriores devem ser reutilizadas diretamente. 
# A ideia é mostrar que, como cada parte já foi construída antes, resolver o problema completo fica muito mais simples



def cabecalho(nome_da_loja):
    print(nome_da_loja)
    print("Sistema de Atendimento")

nome_da_loja = "Laerte Padarias"

def cliente(nome_do_cliente):
    print(nome_do_cliente)

nome_do_cliente = input("Insira seu nome: ")

def comissao(valor_venda):
    valor_venda = valor_venda * 0.05
    return valor_venda
valor_venda = float(input("Insira o valor da venda: "))

comissao(valor_venda)

def calcular_valor_final(valor_produto, desconto):
    resultado = valor_produto * (1 - desconto / 100)
    return resultado

valor_produto = float(input("Insira o valor do produto: "))
percentual_desconto = float(input("Digite a porcentagem de desconto: "))

preco_final = calcular_valor_final(valor_produto, percentual_desconto)

cabecalho(nome_da_loja)

cliente(nome_do_cliente)

print("O preço com desconto é: ", preco_final)

print("A comissao é: ", comissao(valor_venda))

