
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12

print(maior_idade, crianca, adolescente)




print("CÁLCULO DE SEU IMC")

altura = float(input ("Digite sua altura: "))
peso = int(input('Digite seu peso: '))

calculo = peso / (altura*altura)




print('{:.2f}'.format(calculo))

if calculo < 18.5:
    print('Seu IMC é {:.2f}'.format(calculo), end="\n")
    print('Classificação: MAGREZA')
elif calculo >= 18.5 & calculo <= 24.9:
        print('Seu IMC é {:.2f}'.format(calculo), end="\n")
        print("Classificação: NORMAL")

elif calculo >= 25.0 & calculo <= 29.9:
    print('Seu IMC é {:.2f}'.format(calculo), end="\n")
    print('Classificação: SOBREPESO')
elif calculo >= 30.0 & calculo <= 39.9:
    print('Seu IMC é {:.2f}'.format(calculo), end="\n")
    print('Classificação: OBESIDADE')
else:
    print('Seu IMC é {:.2f}'.format(calculo), end="\n")
    print('Classificação: OBESIDADE GRAVE')


