import random
dibujo = ['''

       +---+
       |   |
           |
           |
           |
           |
           =========''', '''

        +---+
        |   |
        O   |
            |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
        |   |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|   |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
            |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
            =========''', '''

        +---+
        |   |
        O   |
       /|\  |
       / \  |
            | PERDISTE :v/
            =========''']
lista = '''perro gato elefante perico jaguar leon lobo aguila'''
def buscaPalabra():
    palabra = lista.split()
    rango = random.randint(0,len(palabra)-1)
    return palabra [rango]
def main():
    palabra = buscaPalabra()
    palabra1 = []
    palabra2 = []
    for i in palabra:
        palabra1.append(i)
        palabra2.append('__')
    contaDibujo = 0
    print(dibujo[contaDibujo])
    print(','.join(palabra2))
    while True:
        entrada = input("Bienvenido al juego del ahorcado: " + "ingrese las letras...suerte (: \n")
        conta = -1
        llave = False
        for i in palabra:
            conta += 1
            if entrada == i:
                palabra2[conta] = i
                llave = True
        if palabra1 == palabra2:
            print('Felicidades ganaste ^w^ \n')
            break
        if contaDibujo >=5 and llave != True:
            print(dibujo[6])
            print('perdiste',''.join(palabra1))
            break
        elif llave != True:
            contaDibujo += 1
        print(dibujo[contaDibujo])
        print(','.join(palabra2))
main()
