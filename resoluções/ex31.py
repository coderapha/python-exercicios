distancia = float(input('Qual é a distância da viagem em km: '))

# if distancia <= 200:
#     valor = distancia * 0.50
# else:
#     valor = distancia * 0.45

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da passagem para {}km é de R$:{:.2f}'.format(distancia, valor))
