#utilizei a mesma forma que aprendi na video aula porem eu faria diferente. Definiria de cara a variavel num
# (sep="_") coloca o separador obrigatorio
#nova att informar se chute foi alto ou baixo
import random
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,51)
total_de_tentativas = 5

while (total_de_tentativas > 0):
    print(total_de_tentativas,'tentativas restantes')
    chute_str = input("\n Digite o seu número: ")
    print("\n Você digitou: ", chute_str)
    chute = int(chute_str)

    if (numero_secreto == chute):
        print("\n Você acertou!")

    else:
        if (chute > numero_secreto):
            print("\n Você errou! O seu chute foi maior que o número secreto.")
        elif (chute < numero_secreto):
            print('\n Você errou! O seu chute foi menor que o numero secreto.')

    total_de_tentativas = total_de_tentativas -1

print("\n*********************************")
print("Fim do jogo")
print("*********************************")