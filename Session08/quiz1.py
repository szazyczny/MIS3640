#Sarah Zazyczny Quiz 1 9/15/18

"""
Question 1:
If the number, n, is divisible by 4, return True; 
return False otherwise. Return False if n is divisible by 100 
(for example, 1900); the only exception is when n is divisible 
by 400(for example, 2000), return True.
"""


def is_special(n):
    """
    If the number, n, is divisible by 4 
    (for example, 2020), return True. 
    Return False if n is divisible by 100 (for example, 300); 
    the only exception is when n is divisible by 
    400(for example, 2400), return True.
    """
    n = n/4
    if n == 0:
        return True
    else:
        n = n / 100
        if n == 0:
            return False
        n = n / 4
        elif n == 0:
            return True
        else:
            return False


# When you've completed your function, uncomment the
# following lines and run this file to test!


print(is_special(2020))
print(is_special(300))
print(is_special(2018))
print(is_special(2000))


"""
-----------------------------------------------------------------------
Question 2:
"""


# def detect(a, b, n):
#     """
#     Returns True if either a or b is n, 
#     or if the sum or difference or product of a and b is n. 
#     """
#     if a == n or b == n:
#         return True
#     else:
#         if a + b == n:
#             return True
#         elif abs(a - b) == n:
#             return True
#         elif a * b == n:
#             return True
#         else:
#             return False


# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(detect(2018, 9, 2018))
# print(detect(2017, 1, 2018))
# print(detect(1009, 2, 2018))
# print(detect(2020, 2, 2018))
# print(detect(2017, 3, 2018))

"""
-----------------------------------------------------------------------
Question 3:
Write a function with loops that computes the sum of all cubes 
of all the odd numbers between 1(inclusive) and 
n (inclusive if n is not even).
"""

def sum_cubes_of_odd_numbers(n):
    result = 0
    for n in range(1, n, 2):        
        if n % 2 == 1:
            result = result + n**3
    print('the sum of all cubes of odd numbers is:', result)
        



# When you've completed your function, uncomment the
# following lines and run this file to test!

# print(sum_cubes_of_odd_numbers(1))
# print(sum_cubes_of_odd_numbers(10))