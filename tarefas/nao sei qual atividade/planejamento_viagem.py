# distância da viagem (km)
# consumo do carro (km/l)
# preço do combustível (R$/l)
# Calcule o quantidade de litros necessários para a viagem, e o custo total da viagem. Imprima os resultados na tela.
# Saída esperada:
# Planejamento de viagem
# ----------------------
# Litros necessários: ...
# Custo estimado: ...

distancia = (int(input("Digite a distâcia da viagem: ")))
consumo = (int(input("Digite o consumo do carro: ")))
preco = (int(input("Digite o preço do combustivel: ")))
litros = 0
litros = distancia // consumo 
total = 0
total = litros * preco

print("Planejamento da viagem:")
print("-----------------------")
print("Litros necessarios:", litros)
print("Custo estimado", total)
