#Exercise 1
#What is the index of 'Apple'? 'Lisa'? 'On Rail'?

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']    
]

#L[0][0] #Apple
#L[2][-1] #Lisa
#L[1][2][1] #On Rail


#TRAVERSING LIST
AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
#print(AFC_east, numbers, empty)

for team in AFC_east:
    #print(team)


numbers = [2, 0, 1, 6, 9]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
#print(numbers)     #prints list * 2 = [4, 0, 2, 12, 18]

#what is len of list
my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))     #prints length of list = 4


#LIST OPERATIONS
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    #prints both lists in one single list [1, 2, 3, 4, 5, 6]

#[0] * 4    #prints list = [0, 0, 0, 0]

#['Tom Brady', 'Bill Belichick']*3  #prints list 3 times

#LIST SLICES
t = ['a', 'b', 'c', 'd', 'e', 'f']
#How do we get ['b', 'c']? ['a', 'b', 'c', 'd']? ['d', 'e', 'f'] ? 
# The entire list?
t[1:3]  # ['b', 'c']
t[0:4]  # ['a', 'b', 'c', 'd']
t[:4]   # ['a', 'b', 'c', 'd']
t[-3:]  # ['d', 'e', 'f']
t[3:]   # ['d', 'e', 'f']
t[::2]  # ['b', 'd', 'f']
t[1::2] #['b', 'd', 'f']
t[::3] #start from beginning, then 3
#first one is where to start :defaultend: step length


t = ['a', 'b', 'c', 'd', 'e', 'f']
#t[1:3] = ['x', 'y']     #replaces index 1 and 2, prints ['a', 'x', 'y', 'd', 'e', 'f']
#print(t)

t[1] = ['g', 'h']
t

#EXERCISE 2
#Read the documentation of the list methods at https://docs.python.org/3/tutorial/datastructures.html#more-on-lists. You might want to experiment with some of them to make sure you understand how they work. append, extend and sort are particularly useful.
#how can we combine 2 lists together 
t = ['a', 'b', 'c', 'd', 'e', 'f']
x = ['g', 'h']
#t.append(x)
t.extend(x) #combines the lists
t


# Example of list methods
#append adds argument as an element
t = ['a', 'b', 'c']
t.append('d')
#print(t)       #adds d to list

#EXERCISE 3
#Finish list_exercises.py

#MAP REDUCE FILTER
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

t = [1, 2, 3]
#print(sum(t))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

#DELETING ELEMENTS
t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
# print(x)
# print(t)


x = t.pop()
# If you don’t provide an index, 
# it deletes and returns the last element.
# print(x)
# print(t)

t = ['a', 'b', 'c', 'd', 'e']
del t[1:3]
# print(t)

t = ['a', 'b', 'c']
t.remove('b')
#print(t)


#LISTS AND STRINGS
team = 'Patriots'
t = list(team)
# print(t)

team = 'New England Patriots'
t = team.split()
# print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
#print(t)

t = ['New', 'England', 'Patriots']
team = ' '.join(t)
#print(team)

#Q. How do we get 'New!!England!!Patriots'?

#OBJECTS AND VALUES
a = 'banana'
b = 'banana'

a is b

a = [1, 2, 3]
b = [1, 2, 3]
a is b

a = [1, 2, 3]
b = a
b is a

b[0] = 'something else'
#print(a)

