from colorama import init, Back, Style, Fore

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
y = Back.YELLOW
g = Back.GREEN
bl = Back.BLACK
fr = Fore.RED
fg = Fore.GREEN
fy = Fore.YELLOW
fb = Fore.BLUE
fw = Fore.LIGHTWHITE_EX
fbl = Fore.BLACK
rs = Style.RESET_ALL


def flag(f):
    print(cp)
    f()
    print('_#_')


def france():
    c = [b, w, r]
    for i in range(9):
        for e in c:
            print(e + ' ' * 10 + rs, end='')
        print()


def thai():
    line = 40
    c = [r, w, b]
    ind = [0, 1, 2, 2, 1, 0]
    for e in ind:
        for i in range(2):
            print(c[e] + ' ' * line + rs)


def usa():
    s = ' '
    for i in range(13):
        if i % 2 and i < 7:
            print(b + ' *' * 7 + s + w + s * 27 + rs)
        elif i % 2 == 0 and i < 7:
            print(b + '* ' * 7 + s + r + s * 27 + rs)
        elif i % 2:
            print(w + s * 42 + rs)
        else:
            print(r + s * 42 + rs)


def rus():
    c = [w, b, r]
    for i in range(3):
        for e in range(3):
            print(c[i] + ' ' * 30 + rs)


def indonesia():
    c = [r, w]
    for i in range(2):
        for e in range(5):
            print(c[i] + ' ' * 30 + rs)


def sweden():
    c = 10
    for i in range(c):
        for e in range(c+5):
            if 3 < e < (c-4) or 3 < i < (c-4):
                s = "\033[43m" + '  '
            else:
                s = "\033[44m" + '  '
            print(s + "\033[0m", end='')
        print()

def congo( el=chr(11203)):
    for i in range(10):
        print(fg + el * (27 - (i*3)) + fy + el * 5 + fr + el*(i*3), rs)

def czech( el=chr(11203)):
    for i in range(10):
        if i < 5:
            print(fb + el * (i*3) + fw + (el *(27 -i*3)), rs)
        else:
            print(fb + el * (27 - i * 3) + fr + (el * (i * 3)), rs)

def guyana(el=chr(11203)):
    for i in range(11):
        if i <= 5:
            print(fr + el * (i*3) + fbl +el + fy + el * i*3 + fw + el + fg + (el *(30 -i*6)), rs)
        else:
            print(fr + el * (27 - (i-1) * 3) + fbl + el + fy + el * (27 - (i-1)*3) + fw + el + fg + (el * ((i-5) * 6)), rs)


def dubai(sym=' '):
    for i in range(9):
        if i < 3:
            print(r + sym * 8 + g + sym * 21, rs)
        elif 2 < i < 6:
            print(r + sym * 8 + w + sym * 21, rs)
        else:
            print(r + sym * 8 + bl + sym * 21, rs)

country = {'rus': rus, 'usa': usa, 'thai': thai, 'france': france,
 'indonesia': indonesia, 'sweden': sweden, 'congo': congo, 'czech': czech,
'guyana': guyana, 'dubai': dubai}
# print('rus,', 'usa,', 'thai,', 'france,', 'indonesia,', '"stop"')
dictkeys = [i for i in country.keys()]

def outline():
    def inner():
        for i, e in enumerate(dictkeys):
            print(e + ', ', end='')
            if (i + 1) % 5 == 0:
                print()
        print('"stop" to exit')
    return inner

out = outline()
out()

while True:
    cp = input('Input country: ')
    if cp in country.keys():
        flag(country[cp])
    elif cp == 'stop':
        break
    else:
        print(out())
