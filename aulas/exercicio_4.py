# Um sistema de avaliação classifica o desempenho de um aluno com base na nota final (0 a 100).
# As classificações são as seguintes:
# 90 a 100 → Excelente
# 70 a 89 → Bom
# 50 a 69 → Regular
# abaixo de 50 → Insuficiente
# O programa deve ler a nota do aluno e mostrar apenas uma classificação.

nota =  (int(input("Digite a sua nota: ")))

if nota > 100:
    print("Nota inválida.")
elif nota <= 100 and nota >= 90:
    print("Nota excelente!")
elif nota <= 89 and nota >= 70:
    print("Nota boa!")
elif nota <= 69 and nota >= 50:
    print("Nota regular.")
else: 
    print("Nota Insuficiente")

print("--------------------")

print("Sua nota é: ", nota)