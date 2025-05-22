# Dias do mês (calendário 2025)


#janeiro = 1
jan = 31

#fevereiro = 2
fev = 28

#março = 3
mar = 31

#abril = 4
abr = 30

#maio = 5
mai = 31

#junho = 6
jun = 30

#julho = 7
jul = 31

#agosto = 8
ago = 31

#setembro = 9
set = 30

#outubro = 10
out = 31

#novembro = 11
nov = 30

#dezembro = 12
dez = 31

# Aqui vai receber o mês, conferir se é valido (1 até 12)
# Depois vai receber a data e validar de acordo com o mês














mesInicial = int(input('Defina o mês inicial: '))

# Aqui valida o mês e atribui o nome (para a mensagem de data inválida)
if 1 <= mesInicial <= 12:
    if mesInicial == 1:
        mesErrado = 'janeiro'
    if mesInicial == 2:
        mesErrado = 'fevereiro'    
    if mesInicial == 3:
        mesErrado = 'março'
    if mesInicial == 4:
        mesErrado = 'abril'
    if mesInicial == 5:
        mesErrado = 'maio'
    if mesInicial == 6:
        mesErrado = 'junho'
    if mesInicial == 7:
        mesErrado = 'julho'
    if mesInicial == 8:
        mesErrado = 'agosto'
    if mesInicial == 9:
        mesErrado = 'setembro'
    if mesInicial == 10:
        mesErrado = 'outubro'
    if mesInicial == 11:
        mesErrado = 'novembro'
    if mesInicial == 12:
        mesErrado = 'dezembro'



    diaInicial = int(input('Defina o dia inicial: '))
    if 1 <= diaInicial <= 31:
        
        mesFinal   = int(input('Defina o mês final: '))
        if 1 <= mesFinal <= 12:
            if mesFinal == 1:
                mesErrado = 'janeiro'
            if mesFinal == 2:
                mesErrado = 'fevereiro'    
            if mesFinal == 3:
                mesErrado = 'março'
            if mesFinal == 4:
                mesErrado = 'abril'
            if mesFinal == 5:
                mesErrado = 'maio'
            if mesFinal == 6:
                mesErrado = 'junho'
            if mesFinal == 7:
                mesErrado = 'julho'
            if mesFinal == 8:
                mesErrado = 'agosto'
            if mesFinal == 9:
                mesErrado = 'setembro'
            if mesFinal == 10:
                mesErrado = 'outubro'
            if mesFinal == 11:
                mesErrado = 'novembro'
            if mesFinal == 12:
                mesErrado = 'dezembro'

            diaFinal   = int(input('Defina o dia final: '))
            if 1 >= diaFinal <= 31:
                print('holder')


























                
            else: print('Dia ',diaFinal,' de ', mesErrado, ' não é uma data válida.' )
        else: print('Mês inválido. Digite um mês entre 1 e 12.' )
    else: print('Dia ',diaInicial,' de ', mesErrado, ' não é uma data válida.' )
else: print('Mês inválido. Digite um mês entre 1 e 12.')
