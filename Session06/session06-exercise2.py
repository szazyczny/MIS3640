#EXERCISE 2
#know how to write FACTORIAL AND FIBONACCI RECURSIONS

#2.1 Write a program, factorial.py to compute a factorial of an integer, n.
# fact(n) = fact(n-1) * n
# fact(3) 1*2*3
# fact(2) 1*2
# fact(1) 1
def fact(n):
    if n == 1:
        return 1
    else: return fact(n-1)*n

print(fact(10))

#2.2 Write a program, fibonacci.py to compute the Fibonacci number of an integer , n.
#fibonacci numbers: 1, 1, 2, 3, 5, 8... find 6th fibonacci
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)

def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6)) #equal to 8


#NEED TO REDO THESE
#2.3 The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.
#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:
# If b = 0, then the answer is a
# Otherwise, gcd(a, b) is the same as gcd(b, a % b)
# Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.

#using Euclid algorithm

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)


#2.4 Tower of Hanoi
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")