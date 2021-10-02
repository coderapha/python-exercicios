nome = str(input('Digite seu nome completo: ')).title().strip()
objNome = nome.split()
print('Seu primeiro nome é: {}'.format(objNome[0]))
print('Seu último nome é: {}'.format(objNome[len(objNome) - 1]))
