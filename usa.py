from colorama import init, Fore

init()
r = Fore.RED
w = Fore.LIGHTWHITE_EX
b = Fore.BLUE

def am():
    print('USA')
    for i in range(13):
        if i % 2 and i < 7:
            print(b + ' *'* 7 + ' ' + w + 'W'*30)
        elif i % 2 != True and i < 7:
            print(b + '* ' * 7 + ' ' + r + 'W' * 30)
        elif i % 2:
            print(w + 'W'* 45)
        else:
            print(r + 'W' * 45)
    print(w + '_#_')

am()
