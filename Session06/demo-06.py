#CONDITIONALS

#IF ELSE CONDITIONAL
# age = input('please enter your age')   #need this line to define what age is, need input
# if int(age) >= 18:       #boolean statement, find out if true or false, MUST convert age to integer
#     print('adult')
# else:                   #do not need to repeat int(age), 2 clear scenarios one above and one under 18
#     print('teenager')

#CHAINED CONDITIONALS
#3 scenarios
# age = input('please enter your age')   
# if int(age) >= 18:       
#     print('adult')
# elif int(age) >= 6:
#     print('teenager')
# else:                  
#     print('child')

#CHECK IF LOGIC MAKES SENSE
#code is executed line by line so this case will print the first true - teenager, never reaches end of code
# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

#NESTED CONDITIONALS
#under if or else there is another if or else block, 3 scenarios
# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')
# #elif can be used to get same result
# if x == y:
#     print('x and y are equal')
# elif x < y:
#     print('x is less than y')
# else:
#     print('x is greater than y')


#EXERCISE 1.1:Create a BMI calculator using if/elif
# def calculate_bmi(weight, height):
#     ''' 
#     calculate bmi for given weight (lb) and height (in^2). 
#     '''
#     bmi = 730 * (weight / (height * height))
#     if bmi <= 18.5:
#         print('underweight')
#     elif 18.5 < bmi <= 25:
#         print('normal weight')
#     elif 25 < bmi < 30:
#         print('overweight')
#     else:
#         print('obesity')

# weight = input('please enter weight')
# height = input('please enter height')

#EXERCISE 1.2
#Assume that two variables, varA and varB, are assigned values, either numbers or strings. Write a piece of Python code that prints out one of the following messages
#python isinstance 
def compare(varA, varB):
    if isinstance(varA, str) or isinstance (varB, str):
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA == varB:
            print('equal')
        else:
            print('smaller')

a = 'hello'
b = 3
c = 5

compare(a, b)
compare(b, c)

#RECURSION - function that calls itself
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(5)

#same function name taking in 2 parameters
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('hi', 3)



