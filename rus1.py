from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL

def shift(line=30, side=3, el='#'):
    print('Rus')
    c = [w, b, r]
    for i in range(side):
        for e in range(side):
            print(c[i] + el * line + rs)
    print(w + '_#_')

shift(el=' ')
