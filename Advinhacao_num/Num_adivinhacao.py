#utilizei a mesma forma que aprendi na video aula porem eu faria diferente. Definiria de cara a variavel num
# (sep="_") coloca o separador obrigatorio
#nova att informar se chute foi alto ou baixo

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

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

print("\n*********************************")
print("Fim do jogo")
print("*********************************")