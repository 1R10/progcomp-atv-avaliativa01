# Valor errado. Lembrar de corrigir

minutos = int(input('Quantidade de minutos que o veículo ficou no estacionamento: '))
horas   = minutos/60
valor = 0
print ('Como você ficou por ', horas, ' horas...')

if horas > 12: # Se a hora for +12 ele nem precisa perder tempo com o resto do código
    print('O valor a ser pago é de R$30,00.')

elif horas <= 2: # Até duas horas
        valor = horas * 8

elif (horas >2 ) and (horas <= 4): # se for maior que duas horas ele já pula pra esse elif que soma o valor e reduz as 2 horas que precisam ser multiplicadas
      valor = 16 + ((horas - 2) * 5)

elif (horas > 4) and (horas <= 12): # Mesma coisa, mas entre 4h e 1 milésimo de segundo e 12h
      valor = 16 + 10 + ((horas - 4) * 3)

print('O valor a ser pago é de R$', round(valor, 2))
