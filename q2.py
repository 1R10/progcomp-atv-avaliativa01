# Coleta as notas dos 4 bimestres
bim1 = float(input('Insira a nota do 1° bimestre: '))
bim2 = float(input('Insira a nota do 2° bimestre: '))
bim3 = float(input('Insira a nota do 3° bimestre: '))
bim4 = float(input('Insira a nota do 4° bimestre: '))
mediaDisciplina = (2*bim1 + 2*bim2 + 3*bim3 + 3*bim4)/10 # Soma as 4 notas com seus pesos e divide por 10

if mediaDisciplina > 59:
    print('Parabéns! O aluno foi aprovado.')

if mediaDisciplina <= 59: # Nota abaixo da média/60
    if mediaDisciplina >= 20: # Critério de recuperação
        notaRecup = float(input('Insira a nota da recuperação: '))
        media_Final = (mediaDisciplina +  notaRecup)/2

        if media_Final > 60:
            print('Parabéns! O aluno foi aprovado.')
        else: print('O aluno foi reprovado')

    if mediaDisciplina < 20:
        print('O aluno reprovou e não tem direito à recuperação.')
