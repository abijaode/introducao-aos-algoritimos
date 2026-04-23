# Crie uma função chamada calcular_situacao(nota) que receba uma nota de 0 a 100 e retorne:

# "Aprovado", se a nota for maior ou igual a 70;
# "Recuperação", se a nota estiver entre 50 e 69;
# "Reprovado", caso contrário.
# No programa principal:

# leia uma nota;
# exiba a situação retornada.


def calcular_situacao(nota):
    if nota >= 70:
        print("Aprovado")
    elif nota < 70 and nota >= 50:
        print("Recuperação")
    else:
        print("Reprovado")

nota = int(input("Digite sua nota: "))

calcular_situacao(nota)