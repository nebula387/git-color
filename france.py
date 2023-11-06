from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL


def france():
    print('Fr')
    sym = ' '
    col = [b, w, r]
    line = 12
    row = 10
    for i in range(row):
        print(b+sym*line + w+sym*line + r+sym*line + rs)
    print('_#_')


france()
