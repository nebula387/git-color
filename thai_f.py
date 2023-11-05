from colorama import init, Fore

init()
r = Fore.RED
w = Fore.LIGHTWHITE_EX
b = Fore.BLUE


def flag(el='#'):
    line = 20
    c = [r, w, b]
    ind = [0, 1, 2, 2, 1, 0]
    print('Thai')
    for i in ind:
        print(c[i] + el * line)
    print(w + '_#_')

flag(el='W')
