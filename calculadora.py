while True:

    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    op = input('digite a operação: (+ - * /) ')
    
    numeroValidos = None
    n1 = 0
    n2 = 0

    try:
        n1 = float(numero1)
        n2 = float(numero2)

        numeroValidos = True

    except:
        ...

    if numeroValidos is None:
        print('Numero invalido')
        continue

    operadorValido = '+-*/ '

    if op not in operadorValido:
        print('Operador invalido :')
        continue

    if len(op) > 1:
        print('Digite apenas um operador')
        continue

    print('Efetuando a conta ...... ')

    if op == '+':
        print(f'{n1} + {n2} = ', n1 + n2)
    
    elif op == '-':
        print(f'{n1} - {n2} = ', n1 - n2)
    
    elif op == '*':
        print(f'{n1} * {n2} = ', n1 * n2)

    elif op == '/':
        print(f'{n1} / {n2} = ', n1 / n2)

    else:
        print('Erro não tratado .........')


    sair = input('Deseja sair ? [s]im: ')
    sair = sair.lower().startswith('s')

    if sair is True:
        break
