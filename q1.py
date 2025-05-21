nCompleto = int(input('Digite um número de 4 dígitos entre 0 - 9999: '))
if nCompleto >= 10000:
    print('O número não pode estar acima de 9999.')
if nCompleto < 0:
    print('O número não pode estar abaixo de 0.')

# O número é dividido de acordo com sua casa decimal 
# (milhar, dezena, centena e unidade)
# o nCompleto será reduzido até virar apenas a unidade
elif  0>= nCompleto >= 9999:
    milhar = nCompleto//1000
    nCompleto = nCompleto - milhar*1000

    centena = nCompleto//100
    nCompleto = nCompleto - centena*100

    dezena = nCompleto//10
    nCompleto = nCompleto - dezena*10

    unidade = nCompleto # Troquei o nome apenas para uma melhor leitura do código

    soma = milhar + centena + dezena + unidade
    print('A soma de ', milhar, '+ ', centena, ' + ', dezena, ' + ',unidade, ' = ', soma )
