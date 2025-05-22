nCompleto = int(input('Digite um número de até 4 dígitos: '))

if nCompleto >  9999:
    print('O número não pode ser maior que 9999.')
if nCompleto < -9999:
    print('O número não pode ser menor que -9999')
elif -9999 <= nCompleto <= 9999 :
# O número é dividido de acordo com sua casa decimal 
# (milhar, dezena, centena e unidade)
# o nCompleto será reduzido até virar apenas a unidade

# Se o número for negativo, será transformado em positivo para a soma dos ALGARÍSMOS

    if nCompleto < 0:
        nCompleto = nCompleto *(-1)
    milhar = nCompleto//1000                    # 1234//1000 = 1
    nCompleto = nCompleto - milhar*1000         # 1234 - 1000 =  234
    
    centena = nCompleto//100                    # 234//100 = 2
    nCompleto = nCompleto - centena*100         # 234 - 200 = 34
    
    dezena = nCompleto//10                      # 34//10 = 3
    nCompleto = nCompleto - dezena*10           # 34 - 30 = 4

    unidade = nCompleto # Troquei o nome apenas para uma melhor leitura do código

    soma = milhar + centena + dezena + unidade  #soma = 1 + 2 + 3 + 4
