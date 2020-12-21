import time
from os import system, name

g = h = i = j  = 0

def clearScreen():
    # windows OS
    if name == 'nt':
        _ = system('cls')
    # mac & linux
    else:
        _ = system('clear')

        
while g <= 5:
    while h <= 9:    
        while i <= 5:
            while j <= 9:
                clearScreen()
                print(str(g) + str(h) + ":" + str(i)+str(j))
                time.sleep(1)
                j += 1
            j = 0
            i += 1
        i = 0
        h += 1
    h = 0
    g += 1

