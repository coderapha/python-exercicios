frase = str(input('Digite uma frase: ')).upper().strip()
print('Esta frase possui {} letras A'.format(frase.count('A')))
print('A posição da primeira letra A nesta frase é = {}'.format(frase.find('A') + 1))
print('A posição da ultima letra A nesta frase é = {}'.format(frase.rfind('A') + 1))
