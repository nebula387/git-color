from colorama import init, Back, Style

init()
r = Back.RED
w = Back.LIGHTWHITE_EX
b = Back.BLUE
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
            print(b + ' *' * 7 + s + w + s * 30 + rs)
        elif i % 2 == 0 and i < 7:
            print(b + '* ' * 7 + s + r + s * 30 + rs)
        elif i % 2:
            print(w + s * 45 + rs)
        else:
            print(r + s * 45 + rs)


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


country = {'rus': rus, 'usa': usa, 'thai': thai, 'france': france,
 'indonesia': indonesia}
# print('rus,', 'usa,', 'thai,', 'france,', 'indonesia,', '"stop"')
dictkeys = [i for i in country.keys()]

def outline():
    def inner():
        print(dictkeys, '\n', '"stop" to exit')
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
