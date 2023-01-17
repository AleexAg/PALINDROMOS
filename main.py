#Practica palindromos


def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    palabra_inv = palabra[::-1]
    if palabra == palabra_inv:
        return True
    else:
        return False


def principal():
    while True:
        print('*' * 30)
        print('|  DETECTOR DE PALINDROMOS  |')
        print('INGRESE "0" PARA CERRAR EL PROGRAMA')
        palabra = input('Ingrese una palabra: ')
        print('*' * 30)
        if palabra != '0':
            print('Analizando.....')
            resultado = palindromo(palabra)

            if resultado:
                print('-' * 30)
                print(f'la plabra "{palabra}" es palindromo')
                print('-' * 30)
            else:
                print('-' * 30)
                print(f'la plabra "{palabra}" no es palindromo')
                print('-' * 30)
        else:
            print('Cerrando programa...')
            break

if __name__ == '__main__':
    principal()
