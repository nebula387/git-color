from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL
col = [b, w, r]

def france(s):
    row = 9
    line = 10
    sym = ' '
    print('FR')
    for i in range(row):
        for e in s:
            print(e+sym*line+rs, end='')
        print()
    print('_#_')


france(col)
