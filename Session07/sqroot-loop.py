#Copy the loop from above and encapsulate it in a function 
#called mysqrt that takes a as a parameter, chooses a 
# reasonable value of x, and returns an estimate of the 
# square root of a.

#To test it, write a function named test_square_root that prints a table

#NEWTONS ALGORITHM      y = (x + a/x) / 2


epsilon=0.0000001

def mysqrt(a):
    '''
    calculates square root for given value a
    '''
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    print(x)

for a in range (1,10):
      mysqrt(a)



#SOLUTION
import math


def mysqrt(a):
    """
    uses Newton’s method to compute square root of a positive number.
    Args:
        a(int): a positive number
    Returns:
        the square root of a.
    """
    epsilon = 1e-15
    x = 1
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x

# for i in range(1, 10):
#     print('The square root of', i, 'is', mysqrt(i))


def test_square_root(n):
    """
    prints the square root of integers from 1 to n-1
    Args:
        n(int): a positive number
    """

    print('{:3} {:14} {:14} {:14}'.format(
        'a', 'mysqrt(a)', 'math.sqrt(a)', 'diff'))
    print('{:3} {:14} {:14} {:14}'.format(
        '-', '---------', '------------', '----'))
    for a in range(1, n):
        print('{:3.1f} {:<14.12g} {:<14.12g} {:<14.12g}'.format(
            a, mysqrt(a), math.sqrt(a), abs(mysqrt(a) - math.sqrt(a))))


test_square_root(10)