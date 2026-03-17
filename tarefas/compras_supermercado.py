# Um supermercado está desenvolvendo um sistema simples para calcular o valor total de uma compra realizada
# em sua loja online. Durante o processo de compra, o sistema recebe o preço de cada produto que o cliente
# adiciona ao carrinho. Cada vez que um produto é incluído, o valor desse item é informado ao sistema. O cliente
# pode continuar adicionando produtos normalmente e, quando terminar a compra, digita 0 para indicar que não
# deseja incluir mais itens.
# Ao final, o sistema deve calcular o valor total da compra, somando todos os preços informados. Depois disso, o
# programa deve verificar se o cliente terá direito a frete grátis. Caso o valor total da compra seja maior ou igual a
# R$200, o sistema informa que o cliente recebeu frete grátis. Caso contrário, o programa informa que o frete
# será cobrado normalmente.
# Por exemplo, se o cliente informar os valores 50, 30, 120 e depois 0, o total da compra será 200 e o sistema
# deverá informar que o cliente recebeu frete grátis. Já se os valores informados forem 40, 25, 60 e depois 0, o
# total será 125 e o sistema deverá informar que o frete será cobrado.

#------------------------------------------------------------------------------------------------------------------

# Planejamento:

# Receber o preço do produto
# Criar variável total = 0
# Enquanto o preço for diferente de 0:
# Somar o preço ao total
# Pedir novo preço
# Mostrar o valor total da compra
# Verificar se total ≥ 200
# Se sim → frete grátis
# Senão → frete normal
# Informar resultado final

total = 0
valor = 0

valor = float(input("Digite o valor da sua primeira compra: "))


while valor != 0:

    
    total = total + valor
    valor = float(input("Digite o valor do produto, para finalizar a compra digite 0. "))

if total >= 200:
    print("Obrigado pela compra, voce ganhou frete gratis!")

else:
    print("Obrigado pela compra, voce irá pagar o frete padrao.")

print ("Seu total foi: ", total)
    