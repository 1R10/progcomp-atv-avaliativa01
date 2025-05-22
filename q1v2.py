nCompleto = int(input('Digite um número de até 4 dígitos: '))

if nCompleto >  9999:
    print('O número não pode ser maior que 9999.')
if nCompleto < -9999:
    print('O número não pode ser menor que -9999')
else:
# O número é dividido de acordo com sua casa decimal 
# (milhar, dezena, centena e unidade)
# o nCompleto será reduzido até virar apenas a unidade

#if  9999<= nCompleto <= 9999:

    milhar = nCompleto//1000                    # 1234//1000 = 1
    print(milhar)
    nCompleto = nCompleto - milhar*1000         # 1234 - 1000 =  234
    print(nCompleto)
    centena = nCompleto//100                    # 234//100 = 2
    print(centena)
    nCompleto = nCompleto - centena*100         # 234 - 200 = 34
    print(nCompleto)
    dezena = nCompleto//10                      # 34//10 = 3
    print(dezena)
    nCompleto = nCompleto - dezena*10           # 34 - 30 = 4
    print(nCompleto)

    unidade = nCompleto # Troquei o nome apenas para uma melhor leitura do código

    soma = milhar + centena + dezena + unidade  #soma = 1 + 2 + 3 + 4

    print('A soma de ', milhar, '+ ', centena, ' + ', dezena, ' + ',unidade, ' = ', soma )
