# Um laboratório de informática possui regras específicas para acesso durante a noite.
# O programa deve ler:
# idade do usuário
# se possui matrícula ativa (1 = sim, 0 = não)
# se possui autorização especial (1 = sim, 0 = não)
# Regras de acesso:
# Estudantes com matrícula ativa e idade ≥ 18 podem entrar.
# Estudantes com matrícula ativa menores de 18 só entram com autorização.
# Pessoas sem matrícula ativa só entram com autorização.
# O programa deve indicar:
# Acesso permitido
# ou
# Acesso negado


matricula = int(input("Voce possui matricula? (1 = sim, 0 = não) "))

while matricula != 1 and matricula != 0:
        print("Leia Novamente")
        matricula = int(input("Voce possui matricula? (1 = sim, 0 = não) "))

autorizacao = int(input("Voce possui autorizacao? (1 = sim, 0 = não) "))

while autorizacao != 1 and autorizacao != 0:
        print("Leia Novamente")
        autorizacao = int(input("Voce possui autorizacao? (1 = sim, 0 = não) "))

idade = int(input("Digite a sua idade: "))

if autorizacao == 1:
        print("Acesso liberado.")

elif idade >= 18 and matricula == 1:
        print("Acesso liberado.")

else:
        print("Acesso negado.")


