# Crie uma função chamada gerar_resumo_correcao(nota) que receba uma nota e retorne dois valores:

# a classificação de desempenho;
# a situação final do aluno.
# Importante: para resolver este exercício, utilize as funções criadas nos exercícios 7 e 8 dentro da nova função.

# No programa principal:

# leia uma nota;
# chame a função;
# exiba os dois valores retornados.


def gerar_resumo_correcao(nota):

    if nota >= 70:
        print("Aprovado")
    elif nota < 70 and nota >= 50:
        print("Recuperação")
    else:
        print("Reprovado")
    
    if nota >= 90:
        print("Excelente")
    elif nota < 90 and nota >= 70:
        print("Bom")
    elif nota < 70 and nota >= 60:
        print("Regular")
    else:
        print("Insuficiente")

nota = int(input("Digite sua nota: "))

gerar_resumo_correcao(nota)