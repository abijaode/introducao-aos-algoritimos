# Crie um procedimento chamado exibir_cliente(nome) que receba o nome de um cliente e exiba a mensagem:

# Cliente: nome_informado
# No programa principal:

# leia o nome do cliente;
# chame o procedimento passando esse valor.


def cliente(nome_do_cliente):
    print(nome_do_cliente)

nome_do_cliente = input("Insira seu nome: ")

cliente(nome_do_cliente)