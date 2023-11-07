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


def thai():
    line = 40
    c = [r, w, b]
    ind = [0, 1, 2, 2, 1, 0]
    for e in ind:
        for i in range(2):
            print(c[e] + ' ' * line + rs)


flag('Thai', thai)
