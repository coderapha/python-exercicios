from random import shuffle
nome1 = input('Aluno 1: ')
nome2 = input('Aluno 2: ')
nome3 = input('Aluno 3: ')
nome4 = input('Aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
