km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (km * 0.15) + (dias * 60)
print('O preço a ser pago pelo aluguel do carro será: R${:.2f}'.format(valor))
