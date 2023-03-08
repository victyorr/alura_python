

def jogar():
    print("******************************")
    print("Bem vindo no jogo de Forca")
    print("******************************")

    palavara_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]


    enforcou = False
    acertou = False


    print(letras_acertadas)
    #enquanto nao enforcou E nao acertou ( enquanto TRUE E TRUE)
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavara_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count("_"))
        print("Ainda faltam acertar {} letras".format(letras_faltando))

    print("FIM DO JOGO")


if(__name__ == "__main__"):
    jogar()
