# Crie uma função chamada nota_valida(nota) que receba uma nota e retorne:

# True, se a nota estiver entre 0 e 100, inclusive;
# False, caso contrário.
# No programa principal:

# leia uma nota;
# exiba o resultado retornado.


def nota_valida(nota):
    if nota >= 0 and nota <= 100:
        return True
    else:
        return False

nota = int(input("Digite a nota: "))

nota_valida1 = nota_valida(nota)

print (nota_valida(nota))
