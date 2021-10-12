velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('você ultrapassou {:.1f}km do permitido e, por isso, vai ser multado em R$:{:.2f}'.format(velocidade - 80, multa))
else:
    print('você está dentro da velocidade permitida')
