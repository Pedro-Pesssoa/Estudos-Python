#Calculo de IMC -> peso/(altura*altura)
nome = 'Pedro'
peso = 67
altura = 1.70

imc = peso / (altura ** 2)

print(f'{nome}, tem {altura:.2f} de altura, {peso:.1f} de peso\nSeu IMC é {imc:.1f}')
