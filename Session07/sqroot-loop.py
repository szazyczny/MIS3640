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

# import math 
# gen_row = lambda: [ a, mysqrt(a), math.sqrt, math.sqrt - mysqrt for c in range(4) ]
# # 'data' is a nested list comprised of five rows and three columns
# data = [gen_row() for c in range(1,10)]

# # create some column headers
# col_headers = ["cl{}".format(i) for i in range(1, 10)]

# # print the column headers first
# print("{:^8} {:^8} {:^8}".format(*col_headers)

# # now print the rows
# for row in 
#   aligned_row = "{:^8} {:^8} {:^8}".format(*row)
#   print(aligned_row)