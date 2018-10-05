#DICTIONARIES

#Exercise 2
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)



#In the previous example fibonacciCounted, known is created outside the function, so it belongs to the special frame called __main__. Variables in __main__ are sometimes called global because they can be accessed from any function. Unlike local variables, which disappear when their function ends, global variables persist from one function call to the next.
#It is common to use global variables for flags; that is, boolean variables that indicate (“flag”) whether a condition is true.

#Exercise 3
# Find out another global variable that is used inside functions. What is the difference between this global variable and known? Why?
# A. If a global variable refers to a mutable value, you can modify the value without declaring the variable.
# !!BE CAREFUL!!: Global variables can be useful, but if you have a lot of them, and you modify them frequently, they can make programs hard to debug.
# Read more about local and global variables: https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python

