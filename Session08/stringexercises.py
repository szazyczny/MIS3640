#STRING METHODS

team = 'New England Patriots'
new_team = team.upper() #makes uppercase
print(new_team)

team = 'New England Patriots'
index = team.find('a') #prints index for first 'a'
print(index)

print(team.find('En')) #prints indexes for 'En'

print(team.find('a', 10)) #within 10 and end
# str.find(sub[, start[, end]] 
# Return the lowest index in the string where substring sub is 
# found within the slice s[start:end]. Optional arguments 
# start and end are interpreted as in slice notation. 
# Return -1 if sub is not found.
# https://docs.python.org/3/library/stdtypes.html#str.find

name = 'bob'
print(name.find('b', 1, 2)) #print -1, not found
#search in spot 1 because start and 1 and 2 is not inclusive


#EXERCISE 3
# Read the documentation of the string methods at 
# https://docs.python.org/3/library/stdtypes.html#string-methods. 
# You might want to experiment with some of them to make sure you 
# understand how they work. split, strip and replace are particularly useful.

#SPLIT, STRIP, REPLACE
print(team.split(' ')) #['New', 'England', 'Patriots']
print(team.split('e')) #['N', 'w England Patriots']
print(team.strip(' ')) #not working? New England Patriots
print(team.strip('e')) #not working? New England Patriots
print(team.replace('England', 'New')) #New New Patriots
print(team.replace(' ', '~')) #New~England~Patriots
#print(team.replace('a', 'b'[, 1])) QUESTION

#examples of other string methods
print(team.isalnum()) #False
print(team.isalpha()) #False because New England Patriots has spaces
print('team'.isalpha()) #True because team the word is all alpha
print(team.isspace()) #False
print(team.upper()) #NEW ENGLAND PATRIOTS
print(team.lower()) #new england patriots

# Read the examples of String format. 
# https://docs.python.org/3/library/string.html#format-examples

#EXERCISE 4: cheap is $33, free is $34 !
# 1. You walk into a store where each item is priced 
# according to the letters in its name: 'a' costs $1, 
# 'b' is $2, and so on. Write a program that prints a 
# receipt for this wacky store:

# bananas $52   
# rice $35
# paprika $72
# potato chips $78
# ------------------------
# Total $237

a = ord('a') - 96
b = ord('b') - 96
c = ord('c') - 96
n = ord('n') - 96
s = ord('s') - 96
r = ord('r') - 96
i = ord('i') - 96
e = ord('e') - 96
p = ord('p') - 96
k = ord('k') - 96
o = ord('o') - 96
t = ord('t') - 96
h = ord('h') - 96

bananas = b + (a*3) + (n*2) + s
print(bananas)
rice = r + i + c + e
print(rice)
paprika = (p*2) + (a*2) + r + i + k
print(paprika)
chips = p + o + t + a + t + o + c + h + i + p + s
print(chips)

total = bananas + rice + paprika + chips
print(total)

print('bananas ${:d}'.format(bananas))
print('rice ${:d}'.format(rice))
print('paprika ${:d}'.format(paprika))
print('potato chips ${:d}'.format(chips))
print('------------------------')
print('Total ${:d}'.format(total))

#final print of receipt
print('bananas ${:d}'.format(bananas), 'rice ${:d}'.format(rice), 'paprika ${:d}'.format(paprika), 'potato chips ${:d}'.format(chips), '------------------------', 'Total ${:d}'.format(total), sep="\n")
#final print of receipt with decimals
print('bananas ${:.2f}'.format(bananas), 'rice ${:.2f}'.format(rice), 'paprika ${:.2f}'.format(paprika), 'potato chips ${:.2f}'.format(chips), '------------------------', 'Total ${:.2f}'.format(total), sep="\n")


#IN OPERATORS
'a' in team #True
'Boston' in team #False
# Q. What does this function do?
# A. With well-chosen variable names, Python sometimes reads like English. 
#    Try to read this function before you execute it.
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

#DEBUGGING

#EXERCISE 5
#is_reverse function

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

#EXERCISE 6
# Write a function called rotate_word that takes a string and an 
# integer as parameters, and returns a new string that contains the
#  letters from the original string rotated by the given amount.

def rotate_word(string, integer)
    for 