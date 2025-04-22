print('Vamos fazer uma operação matemática')
print('-=-'*20)
nome = str(input('Qual é o seu nome? \n'))
num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))
print('Agora selecione qual será a operação deseja fazer:')
print('-=-'*20)
print('''
[1] - Soma
[2] - Subtração
[3] - Divisão
[4] - Multiplicação
[5] - Potência''' '\n' )
print('-=-'*20)
operacao = int(input('Digite o número da operação: '))
if operacao == 1:
  print(f'Olá {nome} resultado da soma é: {num01+num02}')
elif operacao == 2:
  print(f'Olá {nome} resultado da subtração é: {num01-num02}')
elif operacao == 3:
  print(f'Olá {nome} resultado da divisão é: {num01/num02}')
elif operacao == 4:
  print(f'Olá {nome} resultado da mutiplicação é: {num01*num02}')
elif operacao == 5:
  print(f'Olá {nome} resultado da potência: {num01}, elevado a {num02} é: {num01**num02}')
else:
  print('Operação invalida, tente novamente!')
print('Obrigado por participar e utilizar a nossa calculadora <3')
