str_1 = 'iPAD'
str_2 = 'Babson'
str_3 = 'python'

#only checks the first character 
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print('1')
print(any_lowercase1(str_1))
# True 
print(any_lowercase1(str_2))
# False
print(any_lowercase1(str_3))
# True


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print('2')
print(any_lowercase2(str_1))
# True 
print(any_lowercase2(str_2))
# False
print(any_lowercase2(str_3))
# True

#each iteration changes flag so only care about last iteration
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print('3')
print(any_lowercase3(str_1)) #iPAD false because D is uppercase
# False
print(any_lowercase3(str_2))
# True 
print(any_lowercase3(str_3))
# True 


def any_lowercase4(s):
    flag = False
    for c in s: #checking for any lowercase
        flag = flag or c.islower() #false or true/false
    return flag

print('4')
print(any_lowercase4(str_1))
# True 
print(any_lowercase4(str_2))
# True 
print(any_lowercase4(str_3))
# True 

#checking if entire string is all lowercase
def any_lowercase5(s):
    for c in s:
        if not c.islower(): #checks each character to see if not lowercase
            return False
    return True             #not executing until for loop is completed

print('5')
print(any_lowercase5(str_1)) #iPAD runs the i, then runs P and executes for loop
# False 
print(any_lowercase5(str_2))
# False?
print(any_lowercase5(str_3)) #python returns true because all letters go through the for loop then executes function to return True
# True