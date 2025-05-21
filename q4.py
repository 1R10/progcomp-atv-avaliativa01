diaInicial = int(input('Defina o dia inicial: '))
mesInicial = int(input('Defina o mês inicial: '))
diaFinal   = int(input('Defina o dia final: ')) 
mesFinal   = int(input('Defina o mês final: '))

jan = 31 # Defini os dias do mês (calendário 2025)
fev = 28
mar = 31
abr = 30
mai = 31
jun = 30
jul = 31
ago = 31
set = 30
out = 31
nov = 30
dez = 31


diasDataInicial = 0 # Quantidade total de dias que se passaram desde o início do ano até a data inicial

if mesInicial > 1:
    diasDataInicial += jan
if mesInicial > 2:
    diasDataInicial += fev
if mesInicial > 3:
    diasDataInicial += mar
if mesInicial > 4:
    diasDataInicial += abr
if mesInicial > 5:
    diasDataInicial += mai
if mesInicial > 6:
    diasDataInicial += jun
if mesInicial > 7:
    diasDataInicial += jul
if mesInicial > 8:
    diasDataInicial += ago
if mesInicial > 9:
    diasDataInicial += set
if mesInicial > 10:
    diasDataInicial += out
if mesInicial > 11:
    diasDataInicial += nov
if mesInicial > 12:
    diasDataInicial += dez

diasDataInicial += diaInicial

diasDataFinal = 0 # Quantidade total de dias que se passaram desde o início do ano até a data final

if mesFinal > 1:
    diasDataFinal += jan
if mesFinal > 2:
    diasDataFinal += fev
if mesFinal > 3:
    diasDataFinal += mar
if mesFinal > 4:
    diasDataFinal += abr
if mesFinal > 5:
    diasDataFinal += mai
if mesFinal > 6:
    diasDataFinal += jun
if mesFinal > 7:
    diasDataFinal += jul
if mesFinal > 8:
    diasDataFinal += ago
if mesFinal > 9:
    diasDataFinal += set
if mesFinal > 10:
    diasDataFinal += out
if mesFinal > 11:
    diasDataFinal += nov
if mesFinal > 12:
    diasDataFinal += dez
diasDataFinal += diaFinal

diferenca = diasDataFinal - diasDataInicial # Vai eliminar os dias até a data inicial para que possa ser mostrado no terminal

if diferenca > 1: # Só pra corrigir um erro de sintaxe (plural e singular)
    print('A diferença de dias foi de: ', diferenca, ' dias.')
else:
    print('A diferença de dias foi de: ', diferenca, ' dia.')
