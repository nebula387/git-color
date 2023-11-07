from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL
col = [b, w, r, rs]

def france(s):
    row = 9
    line = 10
    sym = ' '
    for i in range(row):
        print()
        for e in s:
            print(e+sym*line, end='')
    print('_#_')


france(col)
