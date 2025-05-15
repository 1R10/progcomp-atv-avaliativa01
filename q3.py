from random import randint
nSorteado = randint(1,100)

pergunta1 = int(input('A máquina sorteia um número entre 1 e 100. Advinhe qual número foi sorteado: '))
if pergunta1 == nSorteado:
    print('Você acertou! O número era ', nSorteado)
else: 
    pergunta2 = int(input('Segunda tentativa: '))
    if pergunta2 == nSorteado:
        print('Você acertou! O número era ', nSorteado)
    else: 
        pergunta3 = int(input('Terceira tentativa: '))
        if pergunta3 == nSorteado:
            print('Você acertou! O número era ', nSorteado)
        else: 
            pergunta4 = int(input('Ultima tentativa: '))
            if pergunta4 == nSorteado:
                print('Você acertou! O número era ', nSorteado)
            else: print('Você errou. O número era ', nSorteado)
