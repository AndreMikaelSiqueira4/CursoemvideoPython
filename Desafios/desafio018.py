from math import radians,sin,cos,tan

angulo = int(input('Angulo: '))
rad = radians(angulo)
sino = sin(rad)
coss = cos(rad)
tane = tan(rad)

print(f'seu angulo de {angulo} em seno é {sino:.2f}')
print(f'em cosseno é {coss:.2f}')
print(f'em, tangente é {tane:.2f}')
