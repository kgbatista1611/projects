# Calculadora de Python:
'''Soma = 1
   Subtração = 2
   Multiplicação = 3
   Divisão = 4'''
import time
print('--------- Calculadora de Python: ---------\n\n')
print('    1 é soma.')
print('    2 é subtração.')
print('    3 é multiplicação.')
print('    4 é divisão.\n')

opcoes = int(input('Escolha entre 1/2/3/4:'))
num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))

if opcoes == 1:
    soma = num1 + num2
    print('\nSoma:', soma)

elif opcoes == 2:
    subtraia = num1 - num2
    print('\nSubtração:', subtraia)

elif opcoes == 3:
    multiplicacao = num1 * num2
    print('\nMultiplicação:', multiplicacao)

elif opcoes == 4:
    divisao = num1 / num2
    print('\nDivisão:', divisao)

else:
    print('\n', opcoes, 'não é uma opção válida!')

time.sleep(20)

