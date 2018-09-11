#Session 4 Functions

type(42) #int
a = type(2) 
type(a) #type

abs(100)
abs(-1)

max(1, 2, 3, 4, 5)
round(4.24354)
round(4.500000000001) #rounds to 5
round(4.5) #rounds to 4
min(2, 5, 6, 8)

#every character in the system has a corresponding number 
ord('a') #97
ord('c') #99
ord('A') #65
ord('$') #36
chr(25)
chr(82123)
#ord and chr are inverse
chr(ord('A') + 3)
chr(ord('A') + 32)
chr(ord('A') + 32 + 3)


#PYTHON CHALLENGE
2 ** 38

dif = ord('g') - ord('a') 
dif #6
chr(ord('f') + 6) #l
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


#DEFINE OWN FUNCTION
def print_lyrics(): 
    print("Hey Jude. Don't make it bad.") 
    print("Take a sad song and make it better.")
#function name cannot have any spaces, dont forget ()
#must indent 

print_lyrics() 
#print(type(print_lyrics())
#nothing in () so does not need input

def repeat_lyrics():
        print_lyrics()
        print('Na')
        print_lyrics()

repeat_lyrics()

def print_twice(whatever):
    print('first time')
    print(whatever)
    print('the second time')
    print(whatever)

print_twice('Babson')

# def print_twice(name):
#     print('first time')
#     print(name)
#     print('the second time')
#     print(name)

# print_twice('Matthew')
# name = input('Please enter your name:')
# print_twice(name)
# print(whatever)

#function that prints nothing but returns something
def give_me_a_break():
    return 'break'

#print(give_me_a_break())

# def give_me_another_break():
#     str1 = 'break'
#     return str1
#     print('another break')
#only prints break beacuse whenever something is return it wont print anymore


def give_me_another_break():
    str1 = 'break'
    print('another break')
    return str1 #return happens at the end
#prints another break break, because break is returned 

print(give_me_another_break()) #inside function is executed first

# result = print_twice('Bing')
# print(result)


#pass function does nothing

#arguement checking isinstance - see what inputs are taken ie. integer or float

#can return multiple values by separating with ,
import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)