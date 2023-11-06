from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL


def flag(el='#'):
    line = 20
    c = [r, w, b]
    ind = [0, 1, 2, 2, 1, 0]
    print('Thai')
    for i in ind:
        print(c[i] + el * line + rs)
    print(w + '_#_')

flag(el=' ')
