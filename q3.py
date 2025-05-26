from random import randint

nSorteado = randint(1,100)
intervalo1 = 1  # Separando os intervalos que eventualmente vão ser utilizados
intervalo2 = 100

print('') # Não sei se posso usar \nprint('')
print('A máquina vai escolher um número aleatóriamente, de 1-100, e você terá que advinhar qual é.')
print('Em caso de erro, a máquina vai reduzir o intervalo para você ter mais chances de acertar (O número permanece o mesmo, é só uma dica)')
print('Se quiser encerrar o programa, e ver o número sorteado, coloque um número fora do intervalo dado.')
print('Ex: O número está entre 1 e 10: Você coloca 11 pra encerrar')
print('')
print('')
tentativa1 = int(input('Advinhe o número: '))


if 0 < tentativa1 <= 100: # O código só vai rodar se a primeira pergunta for entre o intervalo 1 e 2. Basicamente o código vai ser um loop disso por 4 vezes
    if tentativa1 == nSorteado:
        print('Parabéns, você acertou! O número era ')
    else: # Vai trocar o intervalo mais próximo do número sorteado pela tentativa
        if tentativa1 > nSorteado:
            intervalo2 = tentativa1
        if tentativa1 < nSorteado:
            intervalo1 = tentativa1

            # Segunda tentativa
        print('O intervalo agora está entre: ', intervalo1,' e ', intervalo2)
        tentativa2 = int(input('Segunda tentativa: '))

        if intervalo1 < tentativa2 < intervalo2:
            if tentativa2 == nSorteado:
                print('Parabéns, você acertou! O número era ')
            else:
                if tentativa2 > nSorteado:
                    intervalo2 = tentativa2
                if tentativa2 < nSorteado:
                    intervalo1 = tentativa2

            # Terceira tentativa        
                print('O intervalo agora está entre: ', intervalo1,' e ', intervalo2)
                tentativa3 = int(input('Terceira tentativa: '))
                if intervalo1 < tentativa3 < intervalo2:
                    if tentativa3 == nSorteado:
                        print('Parabéns, você acertou! O número era ')
                    else:
                        if tentativa3 > nSorteado:
                            intervalo2 = tentativa3
                        if tentativa3< nSorteado:
                            intervalo1 = tentativa3
            #Quarta tentativa
                        print('O intervalo agora está entre: ', intervalo1,' e ', intervalo2)
                        tentativa4 = int(input('Quarta e última tentativa: '))
                        if intervalo1 < tentativa4 < intervalo2:
                            if tentativa4 == nSorteado:
                                print('Parabéns, você acertou! O número era ')
                            else:
                                print('Não foi dessa vez. Boa sorte na próxima!')
                        else:
                            print('O número deveria estar entre o intervalo dado. Tente novamente...')        
                else:
                    print('O número deveria estar entre o intervalo dado. Tente novamente...')
        else:
            print('O número deveria estar entre o intervalo dado. Tente novamente...')
else:
    print('O número tem que ser de 1 até 100')
print('O número sorteado foi: ',nSorteado)
