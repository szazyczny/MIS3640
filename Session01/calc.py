# #SESSION 1: PRINTING CALCULATIONS

# #print(8 + 30 + 2018)

# #E2 Q1 - how many seconds = 2562 seconds
# print((42 * 60) + 42)

# #E2 Q2 - how many miles is 10 km = 6.25 miles
# print(10 / 1.6)

# #E2 Q3a - average pace in miles per second = 409.92 mps
# print(2562 / 6.25)
# #E2 Q3b - average pace in miles per minute = 6.832 mpm
# print(409.92 / 60)
# #E2 Q3c - average pace in miles per hour = 8.782201405152225 mph
# print(60 / 6.832)

#SESSION 2 EXERCISES
#The volume of a sphere with radius r is (4/3)πr^3. 
# What is the volume of a sphere with radius 5?
import math
print(math.pi)

r = 5
print(r)

v = (4/3) * math.pi * (r ** 3)
print(v)

print('The volume of a sphere with radius 5 has a volume of {:.2f}'.format(v))