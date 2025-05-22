# Dias do mês (calendário 2025)

jan = 31
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


bloqueioInicial = 0 # Uma chave para bloquear o programa de entrar na parte final se a inicial não for cumprida
mesInicial = int(input('Defina o mês inicial: '))

# Aqui valida o mês e atribui o nome (para a mensagem de data inválida)
if 1 <= mesInicial <= 12:
    if mesInicial == 1:
        mes = 'janeiro'
    
    if mesInicial == 2:
        mes = 'fevereiro'    
    if mesInicial == 3:
        mes = 'março'
    if mesInicial == 4:
        mes = 'abril'
    if mesInicial == 5:
        mes = 'maio'
    if mesInicial == 6:
        mes = 'junho'
    if mesInicial == 7:
        mes = 'julho'
    if mesInicial == 8:
        mes = 'agosto'
    if mesInicial == 9:
        mes = 'setembro'
    if mesInicial == 10:
        mes = 'outubro'
    if mesInicial == 11:
        mes = 'novembro'
    if mesInicial == 12:
        mes = 'dezembro'




    diaInicial = int(input('Defina o dia inicial: '))
    mensagemDeErro = ('Dia', diaInicial,' de ', mes, ' não existe.')

    if mes == 'janeiro':#1
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'fevereiro':#2
        if 1 > diaInicial or diaInicial > 28:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'março':#3
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'abril':#4
        if 1 > diaInicial or diaInicial > 30:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'maio':#5
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'junho':#6
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'julho':#7
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'agosto':#8
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'setembro':#9
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'outubro':#10
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1
    if mes == 'novembro':#11
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1

    if mes == 'dezembro':#12
        if 1 > diaInicial or diaInicial > 31:
            print(mensagemDeErro)
            bloqueioInicial += 1


    if bloqueioInicial == 0:
        mesFinal = int(input('Digite o mês final: '))
        if 1 <= mesFinal <= 12:
            if mesFinal == 1:
                mes = 'janeiro'           
            if mesFinal == 2:
                mes = 'fevereiro'    
            if mesFinal == 3:
                mes = 'março'
            if mesFinal == 4:
                mes = 'abril'
            if mesFinal == 5:
                mes = 'maio'
            if mesFinal == 6:
                mes = 'junho'
            if mesFinal == 7:
                mes = 'julho'
            if mesFinal == 8:
                mes = 'agosto'
            if mesFinal == 9:
                mes = 'setembro'
            if mesFinal == 10:
                mes = 'outubro'
            if mesFinal == 11:
                mes = 'novembro'
            if mesFinal == 12:
                mes = 'dezembro'

            diaFinal = int(input('Defina o dia final: '))
            mensagemDeErro = ('Dia', diaFinal,' de ', mes, ' não existe.')

            if mes == 'janeiro':#1
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'fevereiro':#2
                if 1 > diaFinal or diaFinal > 28:
                    print(mensagemDeErro)
            if mes == 'março':#3
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'abril':#4
                if 1 > diaFinal or diaFinal > 30:
                    print(mensagemDeErro)
            if mes == 'maio':#5
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'junho':#6
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'julho':#7
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'agosto':#8
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'setembro':#9
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'outubro':#10
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'novembro':#11
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)
            if mes == 'dezembro':#12
                if 1 > diaFinal or diaFinal > 31:
                    print(mensagemDeErro)

                if mesInicial <= mesFinal:

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












                else: print('Os meses precisam ser maiores ou iguais. Isto não é uma máquina do tempo.')
        else: print('Mês inválido. Digite um mês entre 1 e 12.')
else: print('Mês inválido. Digite um mês entre 1 e 12.')
