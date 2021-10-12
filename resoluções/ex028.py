from random import randint

computador = randint(0,5)
print('Pensei em um número que está entre 0 e 5. Você Consegue adivinhar qual foi?')
jogador = int(input('Digite sua aposta: '))

if jogador == computador:
    print('\033[32mVocê acertou! Eu pensei em {}'.format(computador))
else:
    print('\033[31mQue pena! Você errou! Eu pensei em {}'.format(computador))
