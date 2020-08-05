# Your code here
import math
import random

pow_cash = {}

def populate_pow_cash():
    for i in range(2, 15):
        pow_cash[i] = {}
        for j in range(3, 7):
            pow_cash[i][j] = math.pow(i, j)

populate_pow_cash()

def slowfun_too_slow(x, y):
    v = pow_cash[x][y]
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

main_cash = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    key = str((x,y))
    if key in main_cash:
        return main_cash[key]
    
    main_cash[key] = slowfun_too_slow(x,y)
    return main_cash[key]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

