from random import randint

nSorteado = randint(1,100)
intervalo1 = 1  # Separando os intervalos que eventualmente vão ser utilizados
intervalo2 = 100
tentativa1 = int(input('A máquina sorteia um número entre 1 e 100. Advinhe qual número foi sorteado: '))
#print(intervalo1 , intervalo2)

if 0 < tentativa1 <= 100: # O código só vai rodar se a primeira pergunta for entre o intervalo 1 e 2. Basicamente o código vai ser um loop disso por 4 vezes
    if tentativa1 == nSorteado:
        print('Parabéns, você acertou!')
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
                print('Parabéns, você acertou!')
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
                        print('Parabéns, você acertou!')
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
                                print('Parabéns, você acertou!')
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
