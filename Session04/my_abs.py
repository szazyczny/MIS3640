#Define a function my_abs to print the absolute value of any number
# def my_abs(n):
#     if n < 0:
#         print(-n)
#     else:
#         print(n)

# my_abs(-5)
# my_abs(4)


#Modify the function my_abs to return the absolute value of any number.
def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

print(my_abs(-5))
print(my_abs(4))

#Modify the function my_abs to first only allow integers and floating numbers, 
#then return the absolute value of any number. 
# You will need a built-in function isinstance() https://docs.python.org/3/library/functions.html#isinstance.


#Define a function quadratic(a, b, c) to solve a quadratic equation: ax2+bx+c=0
def quadratic (a, b, c): 
    pass    #pass function does nothing, needs to be modified