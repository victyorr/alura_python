import random

def jogar():

    print("******************************")
    print("Bem vindo no jogo de Adinhação")
    print("******************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("     NIVEIS DE DIFICULDADE     ")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2 ):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos}")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if(rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute) # abs ignora o sinal do numero entao nao importa se e negativo ou nao
            pontos = pontos - pontos_perdidos
    print("FIM DO JOGO")
    print("O NUMERO ERA", numero_secreto)


if(__name__ == "__main__"):
    jogar()