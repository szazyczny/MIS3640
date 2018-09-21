# #Copy the loop from above and encapsulate it in a function 
# #called mysqrt that takes a as a parameter, chooses a 
# # reasonable value of x, and returns an estimate of the 
# # square root of a.

# #To test it, write a function named test_square_root that prints a table

# #NEWTONS ALGORITHM      y = (x + a/x) / 2

# a = 4
# x = 3
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)



epsilon=0.0000001

def mysqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    print('the square root is:', x)
    
for a in range (1,10):
      mysqrt(a)

# epsilon=0.0000001

# def mysqrt(a):
#     while True:
#         x = a^(1/2)
#         y = (x + a/x) / 2
#         if abs(y-x) < epsilon:
#             break
#         print('the square root is:', x)

# mysqrt(4)