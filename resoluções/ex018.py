from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {}º tem o SENO {:.2f}'.format(angulo, seno))
print('O ângulo de {}º tem o COSSENO {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}º tem a TANGENTE {:.2f}'.format(angulo, tangente))
