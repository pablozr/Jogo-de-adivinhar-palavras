import os
ps = 'salsicha' # palavra secreta
la = '' # letra acertadas
tt = 0 # tentativas totais


while True:
    tt += 1
    tentativa = input('Tente adivinhar a palavra secreta, digite apenas uma letra: ')

    if len(tentativa) > 1:
        print('Digite apenas uma letra')
        continue

    if tentativa in ps:
        la += tentativa

    pf = '' # palavra formada
    for i in ps:
        if i in la:
            pf += i
        else:
            pf += '*'

    print('Palavra formada:', pf)        

    if pf == ps:
        os.system('cls')
        print('Voce acertou!')
        print('A palavra era', ps) 
        print('Total de tentativas:', tt)
        la = ''
        tt = 0
        ps = 'macarrao'      
    






         
