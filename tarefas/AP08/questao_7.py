# Crie uma função chamada classificar_desempenho(nota) que receba uma nota de 0 a 100 e retorne:

# "Excelente" para notas de 90 a 100;
# "Bom" para notas de 70 a 89;
# "Regular" para notas de 60 a 69;
# "Insuficiente" para notas abaixo de 60.
# No programa principal:

# leia uma nota;
# exiba a classificação retornada.

def classificar_desempenho(nota):
    
    if nota >= 90:
        print("Excelente")
    elif nota < 90 and nota >= 70:
        print("Bom")
    elif nota < 70 and nota >= 60:
        print("Regular")
    else:
        print("Insuficiente")

nota = int(input("Digite sua nota: "))

classificar_desempenho(nota)

    