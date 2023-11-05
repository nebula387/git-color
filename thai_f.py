from colorama import init, Fore

init()
r = Fore.RED
w = Fore.LIGHTWHITE_EX
b = Fore.BLUE


def flag(line, el='#'):
    c = [r, w, b]
    for i in range(3):
        print(c[i] + el * line)

    c = c[::-1]
    for i in range(3):
        print(c[i] + el * line)


flag(25, el='W')
