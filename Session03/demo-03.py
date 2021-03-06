#Numbers
len(str(2 ** 1000000)) #len = length, str indicates string

import math
print(math.pi)
print(math.sqrt(85))

import random
print(random.random())
random.choice([1, 2, 3, 4])
random.choice(['rock', 'paper', 'scissors'])

#Strings
print('I\'m \"ok\".')  # Use escape character \
print('I\'m learning\nPython.') #\n creates enter space
print('\\\n\\')

print('\\\t\\')
print(r'\\\t\\')

print('''line1
... line2
... line3''')

#Boolean
True
False

3>2
3>5

3>2 and 3>5

True and True
True and False
False and False

current_time = 4
if current_time > 5:
    print('class is over')
else:
    print('you cannot leave yet')

age = int(input('Please enter your age:')) #convert input into integer
if age >= 21:
    print('yes, you can.')
else:
    print('sorry, you cannot.')



# 3. The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
# import time
# time.time()
# 1437746094.5735958
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time

epochsec = (time.time()) #time since epoch seconds -> make seconds into days 
print(epochsec)
epochmin = (epochsec / 60)
print(epochmin)
epochhours = (epochsec / 60 / 60)
print(epochhours)
epochdays = (epochsec / 60 / 60 / 24)
print(epochdays)
type(epochdays) 


#current time
currenttime = time.localtime(time.time())
print(currenttime)

localtime = time.asctime( time.localtime(time.time()) )
print('Local current time :', localtime)
# print('Local current time : {:%x}' .format(localtime))
# print('Local current time : {:%h:%m:%s}' .format(localtime))
# print(datetime.datetime.today().hour)
# '...{:02d}:{:02d}:{:02d}...'.format(h, m, s)

import datetime
h = datetime.datetime.today().hour
print(h)
m = datetime.datetime.today().minute
print(m)
s = datetime.datetime.today().second
print(s)

print('The local current time is {:02d}:{:02d}:{:02d}, and it has been {:.0f} days since the epoch.' .format(h, m, s, epochdays))


#SOLUTION
import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
