sexo = input('Informe seu sexo (m/f): ')
altura = float(input('Informe sua altura em metros (ex.: 1.75): '))
peso = float(input('Informe o seu peso (em kg): '))

if sexo == 'm':
    peso_ideal = round((72.7 * altura) - 58, 2)
else:
    peso_ideal = round((62.1 * altura) - 44.7, 2)

if peso > peso_ideal:
    print('Voce está acima do seu peso ideal:', peso_ideal)
elif peso < peso_ideal:
    print('Voce está abaixo do seu peso ideal:', peso_ideal)
else:
    print('Voce está no seu peso ideal:', peso_ideal)