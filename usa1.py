from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
rs = Style.RESET_ALL

def usa():
    sim = ' '
    print('USA')
    for i in range(13):
        if i % 2 and i < 7:
            print(b + ' *' * 7 + ' ' + w + sim * 30 + rs)
        elif i % 2 != True and i < 7:
            print(b + '* ' * 7 + ' ' + r + sim * 30 + rs)
        elif i % 2:
            print(w + sim * 45 + rs)
        else:
            print(r + sim * 45 + rs)
    print('_#_')


usa()
