# Criando uma função que leia apenas números - 22.07.2022
def readInt(x):
    sim = False
    y = 0
    while True:
        if x.isnumeric():
            y = int(x)
            sim = True
            print(f'O número digitado foi \033[1;94m{x}.')
        else:
             print('\033[1;91mERRO! Digite um valor válido!')
        if sim:
            break
        return y



# Programa principal
n = readInt(input('Digite um número:'))