#!/usr/bin/env python3
from os import system
from platform import system as os
OS = os()
if OS == 'Windows':
    system('') # Activating colors in Windows command prompt
# colors
RESET = '\033[0m'
WHITE = '\033[47m'
BLUE = '\033[44m'
BLACK = '\033[40m'
bspace = BLACK + ' ' + RESET
wspace = WHITE + ' ' + RESET
# flag
flag = 'Flag of Finland\n' + \
    (top := WHITE + ' ' * 4 + BLUE + ' ' * 2 + WHITE + ' ' * 8 + RESET) + '\n' + \
    BLUE + ' ' * 14 + RESET + '\n' + top
# pattern
cond = lambda i, offsets: 0 in list(map(lambda j: (j + i) % 28, offsets))
gen_offset = lambda length: list(range(length, -length, -1))
gen_line = lambda i: ''.join(map(lambda j: bspace if cond(j, gen_offset(i+7)) else wspace, range(1, 120+1)))
gen_hemicircle = lambda rng: list(map(gen_line, rng))
first = gen_hemicircle(range(1, 4 * 2))
pattern = 'Pattern:\n' + '\n'.join(first) + '\n' + '\n'.join(first[::-1])
# graph
y = lambda x: int(x / 2)
points =  list(map(lambda x: (x, y(x)), range(16)))
graph = 'Graph of the function y = x / 2:\ny\n' + \
    '\n'.join(map(lambda y: \
    ''.join(map(lambda x: \
        bspace if (x, y) in points else wspace, range(16)))[::-1], range(16)))[::-1] + 'x'
# sequence
fp = open('./sequence.txt', 'r')
fr = fp.read().split('\n')
sequence = 'Numbers 5 <= x <= 10 and -10 <= x <= -5:\n' + \
    ', '.join(filter(lambda x: (fx := float(x)) >= 5 and fx <= 10 or fx <= -5 and fx >= -10, fr))
fp.close()
# output
print(flag, pattern, graph, sequence, sep='\n')
