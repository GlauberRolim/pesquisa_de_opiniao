#Limpar a tela
import os
os.system('cls' if os.name == 'nt' else 'clear')

#PESQUISA DE OPINIÃO

RUIM = 0
EXCELENTE = 0
BOM = 0

for pessoas in range(1,11):

    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))
    opiniao = input("Na sua opinião, o atendimento foi RUIM, BOM ou EXCELENTE? ")

    if opiniao == "RUIM":
        RUIM += 1

    elif opiniao == "EXCELENTE":
        EXCELENTE += 1

    else:
        BOM += 1

print(f"A quantidade de respostas RUIM foi {RUIM}.")
print(f"A quantidade de respostas EXCELENTE foi {EXCELENTE}.")
