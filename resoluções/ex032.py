from datetime import date
from random import uniform

ano = int(input('Que ano você quer atualizar? Digite 0 caso queira analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano < 2021:
    tempoVerbal = 'foi'
if ano == 2021:
    tempoVerbal = 'é'
if ano > 2021:
    tempoVerbal = 'será'

# um ano só é bisexto se o resto da divisão dele por 4 for igual a 0 E o resto da divisão dele por 100 for diferente de 0 OU se a divisão dele por 400 for = 0

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} {} um ano bisexto'.format(ano, tempoVerbal))
else:
    print('{} não {} um ano bisexto'.format(ano, tempoVerbal))
