from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL


def flag(c, f):
    print(c)
    f()
    print('_#_')


def france():
    s = [b, w, r]
    for i in range(9):
        for e in s:
            print(e+' '*10+rs, end='')
        print()


flag('FR', france)
