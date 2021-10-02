a = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
area = a * l
tinta = (1 * area) / 2
print('Altura da parede: {}m \nLargura da parede: {}m \nárea da parede: {:.2f}m² \nQuantidade de tinta necessária: {:.1f} litros'.format(a, l, area, tinta))
