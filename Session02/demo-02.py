#SESSION 2: VARIABLES, EXPRESSIONS, AND STATEMENTS

#OUTPUTS
# print('Hello, world!')
# print('Hey Jude, Don\'t make it bad')
# print('The sum is', 2 + 2 + 2 + 2)

#INPUTS
# print('Please enter your name:')   #paramter of function input
# name = input()
# print('Hello,', name)
# #or
# name = input('Please enter your name:')
# print('Hello,', name)

# message = "I learned something cool today"
# n = 100
# pi = 3.14
# print(n) #n = 100

# #DYNAMIC LANGUAGE - variables can be redefined
# a = 123 # a is an integer
# print(a)
# a = 'ABC' # a becomes a string
# print(a)

#ASSIGNMENT - assign old x to new x+2
# x = 10
# x = x + 2 # This does not make sense in mathematics, 
# #but it is perfectly ok in Python.
# print(x)

#WHAT HAPPENS IN RAM
# a = 'ABC' #a is ABC
# b = a #b is ABC
# a = 'XYZ' #a redefined as XYZ
# print(b) #b is still ABC

#OPERATOR BETWEEN STRINGS
# first_name = 'Sarah'
# last_name = 'Zazyczny'
# name = first_name + ' ' + last_name #use space to create space between name strings, creates a space string
# print(name)


# first_name = input('Please enter your first name:')
# last_name = input('Please enter your last name:')
# print('Hello,', first_name + ' ' + last_name)

#print('Hello, {}'.format('world')) #i want a string with hello, {placeholder} then .format means running function on string - replaces {} with word

# name = 'python'
# print('Hello, {}'.format(name))

#print('Congratulations, {:s}, you won {:d}th Academy award.'.format(name, 90))
# s means string, d means integer

#print('Pi equals {}'.format(3.14159265))
#print('Pi equals {:010.2f}'.format(3.14159265))
# f means floating or decimal

#print('Growth rate: {:.2f}%'.format(2.5))

#print('Coordinates of Babson: {lat}, {lon}'.format(lon='71.27W', lat='42.30N'))
# order doesnt matter
