# se o resto da divisão (módulo %) por 2 = a 0, o número é par
# se não, o número é ímpar
numero = float(input('Digite um número: '))
if (numero % 2) == 0:
    print('{} é um número par'.format(numero))
else:
    print('{} é um número ímpar'.format(numero))
