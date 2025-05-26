# Coleta as notas dos 4 bimestres e calcula a média
bim1 = float(input('Insira a nota do 1° bimestre: '))
bim2 = float(input('Insira a nota do 2° bimestre: '))
bim3 = float(input('Insira a nota do 3° bimestre: '))
bim4 = float(input('Insira a nota do 4° bimestre: '))
mediaDisciplina = (2*bim1 + 2*bim2 + 3*bim3 + 3*bim4) / 10

if mediaDisciplina >= 60:
    print('Parabéns! O aluno foi aprovado.')

else: # Menor que 60
    if mediaDisciplina >= 20: # Critério da recuperação
        notaRecup = float(input('Insira a nota da recuperação: '))
        media_Final = (mediaDisciplina + notaRecup) / 2

        if media_Final >= 60:
            print('Parabéns! O aluno foi aprovado.')
        else:
            print('O aluno foi reprovado.')
    else:
        print('O aluno reprovou e não tem direito à recuperação.')
