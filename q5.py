minutos = int(input('Quantidade de minutos que o veículo ficou no estacionamento: '))
valor   = 0
horas   = minutos // 60 # Transforma os minutos em horas
fracao  = minutos  % 60

if fracao > 0: # Vê se há uma fração dos minutos restantes e converte a mesma em +1 hora (se houver)
      horas += 1 

if horas > 12: # Se a hora for +12 ele nem precisa perder tempo com o resto do código
    print('O valor a ser pago é de R$30,00.')

elif horas <= 2: # Até duas horas
        valor = horas * 8

elif horas <= 4: # se for maior que duas horas ele já pula pra esse elif que soma o valor e reduz as 2 horas que precisam ser multiplicadas
      valor = (horas - 2) * 5 + 16

else:
       # Mesma coisa, mas a partir 4h e 1 milésimo de segundo
      valor = (horas - 4) * 3 + 16 + 10

print('O valor a ser pago é de R$', valor)
