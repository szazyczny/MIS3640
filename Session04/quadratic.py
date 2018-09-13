#Define a function quadratic(a, b, c) to solve a quadratic equation: ax^2+bx+c=0
#Discriminant: b^2−4ac

def quadratic(a, b, c):
    ''' 
    return the two roots of a quadratic equation. 
    '''
    d = (b ** 2 - 4 * a * c) ** 0.5 #use discriminant, 0.5 is exponent to get square root
    x = (-b + d) / (2 * a) #solving for x
    return x

    
print(quadratic(1, 6, 9))
print(quadratic(3, 4, 5))


# def quadratic(a, b, c):
#     if :
#         d = (b ** 2 - 4 * a * c) ** 0.5 #use discriminant, 0.5 is exponent to get square root
#          x = (-b + d) / (2 * a) #solving for x
#          return x
#     else:
#         print('No Real Number Solution')
#         return None
        



#two ways to get math package
from math import sqrt #only asking for sqrt, cant use other tools from math module
sqrt(4)
import math #imports all math tools
math.sqrt(4)
math.floor(5.1)
math.pi