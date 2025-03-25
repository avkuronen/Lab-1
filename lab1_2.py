#!/usr/bin/env python3
from os import system
from platform import system as os
from time import sleep
OS = os()
if OS == 'Windows':
    system('') # Activating colors in Windows command prompt
clear = lambda: system('cls') if OS == 'Windows' else system('clear')
# colors
RESET = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
BLACK = '\033[40m'
bspace = BLACK + ' ' + RESET
wspace = WHITE + ' ' + RESET
divisor = 28
dmin, dmax = 28, 31
increasing = True
cond = lambda i, offsets: 0 in list(map(lambda j: (j + i) % divisor, offsets))
gen_offset = lambda length: list(range(length, -length, -1))
gen_line = lambda i: ''.join(map(lambda j: bspace if cond(j, gen_offset(i+7)) else wspace, range(1, 120+1)))
gen_hemicircle = lambda rng: list(map(gen_line, rng))
while True:
    first = gen_hemicircle(range(1, 4 * 2))
    pattern = '\n'.join(first) + '\n' + '\n'.join(first[::-1])
    print(pattern)
    if increasing:
        divisor += 1
        if divisor == dmax:
            increasing = False
    else:
        divisor -= 1
        if divisor == dmin:
            increasing = True
    sleep(0.125)
    clear()
