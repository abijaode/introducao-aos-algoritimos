# Uma disciplina utiliza dois critérios para aprovação:
# média final
# frequência
# O programa deve ler:
# média do aluno
# percentual de frequência
# As regras são:
# Se a frequência for menor que 75%, o aluno está reprovado por falta.
# Caso contrário, analisar a média:
# média ≥ 60 → aprovado
# média entre 40 e 59 → recuperação
# média abaixo de 40 → reprovado por nota
# O programa deve mostrar o resultado final do aluno.
# Desafio adicional
# Versão A: utilizando condicionais aninhadas.
# Versão B: tentando reduzir o número de níveis de aninhamento usando operadores lógicos (and).

media = (float(input("Digite a sua média final: ")))
frequencia = int(input("Digite a sua frequência: "))

if frequencia < 75:
    print("Você foi reprovado por falta.")

elif media >= 60:
    print("Parabéns você foi aprovado!")

elif media >= 40:
    print("Você está de recuperação.")

else:
    print("Você foi reprovado por nota.")