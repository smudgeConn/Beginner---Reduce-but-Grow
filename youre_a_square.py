import math

def is_square(n):    
    print(n)
    if n < 0:
        return False
    elif n == (math.sqrt(n))**2:
        return True
    return False
