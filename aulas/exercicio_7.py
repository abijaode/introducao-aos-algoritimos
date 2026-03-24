# Uma competição escolar de programação classifica participantes com base em:
# pontuação obtida
# tempo gasto na prova
# O programa deve ler:
# pontuação total do participante
# tempo total gasto (em minutos)
# Classificação:
# pontuação ≥ 90 → Ouro
# pontuação ≥ 70 → Prata
# pontuação ≥ 50 → Bronze
# caso contrário → sem medalha
# Regra adicional:
# Se o participante obtiver Ouro e terminar a prova em menos de 120 minutos, ele recebe:
# Participante destaque da competição
# O programa deve mostrar:
# a classificação obtida
# e, se aplicável, o título de destaque

pontuacao = int(input("Pontuação: "))
tempo = int(input("Tempo (min): "))

if pontuacao >= 90:
    print("Classificação: Ouro")

    if tempo < 120:
        print("Participante destaque da competição")

elif pontuacao >= 70:
    print("Classificação: Prata")

elif pontuacao >= 50:
    print("Classificação: Bronze")

else:
    print("Sem medalha")