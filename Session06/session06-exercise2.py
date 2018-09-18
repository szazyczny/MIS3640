#EXERCISE 2

#2.1 Write a program, factorial.py to compute a factorial of an integer, n.
# fact(n) = fact(n-1) * n
# fact(3) 1*2*3
# fact(2) 1*2
# fact(1) 1
def fact(n):
    if n == 1:
        return 1
    else: return fact(n-1)*n

print(fact(3))

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

#2.3 The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.