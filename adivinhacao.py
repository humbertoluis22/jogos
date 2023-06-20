print("**********************************")
print("bem vindo ao jogo de adivinhação!!")
print("**********************************")

numero_secreto = 42
rodada = 1
total_tentivas = 3


while (rodada <= total_tentivas):
    print("Tentativa {} de  {}".format(rodada, total_tentivas))
    chute_str = input("digite o seu numero: ")
    chute = int(chute_str)
    print("vc digitou: ", chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("voce acertou!!")
    else:
        if(maior):
            print("voce errou!!o chute foi maior do que o numero secreto!")
        elif(menor):
            print("voce errou!!o chute foi menor do que o numero secreto!")
    rodada += 1
print("FIM DO JOGO!!")
