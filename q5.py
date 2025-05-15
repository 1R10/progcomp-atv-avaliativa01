minutos = 310 #float(input('Quantidade de minutos que o veículo ficou no estacionamento: '))
horas   = minutos/60 
valor = 0

if horas >= 12:
    print('O valor a ser pago é 30.')
else:
    if horas >= 2:
        valor = horas * 8
