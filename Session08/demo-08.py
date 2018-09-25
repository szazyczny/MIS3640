#STRINGS

team = "New England Patriots"
len(team)    #18 letters with 2 spaces, elements in container
letter = team[1]    #expression in brackets is called an index
print(letter)   #prints e beacuase ALWAYS starts count from 0

print(team[0])
#cannot print team[1.5] or team[1.0] string indices must be integers
print(team[-1])
print(team[19])
#above 2 are the same to print last s beacuse team[20-1] and team[-1]
print(team[-2]) #prints second to last letter t
print(team[-20]) #prints first letter N
print(team[3]) #prints the space

#len(str(2**1000000))
#cannot print len(2**1000000) beacuse not an integer must convert to string

#TRAVERSAL WITH FOR LOOP
index = 0
while index < len(team):
    letter = team[index]
    print(letter)
    index = index + 1

# Another way
for letter in team:
    print(letter)

#duck names
#In Robert McCloskey’s book Make Way for Ducklings, 
# the names of the ducklings are Jack, Kack, Lack, Mack, 
# Nack, Ouack, Pack, and Quack. This loop outputs these names in order:
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)


#STRING SLICES
team = 'New England Patriots'
print(team[0:3]) #New
print(team[0:3]) #New(space)
print(team[0:11]) #New England
print(team[:11]) #New England ^same
print(team[12:20]) #Patriots
print(team[12:]) #Patriots ^same
print(team[4:11]) #England
print(team[11:4]) #blank because it is wrong, there is no index 4 after 11

#string slice taking third index with "step size"
print(team[0:20:2]) #NwEgadPtit - prints every 2 characters
print(team[::2]) #NwEgadPtit ^same
print(team[::-2]) #sora nln e - prints every 2 characters backwards starting from the end

#strings are immutable which means you cannot change an existing string
# team = 'New England Patriots'
# team[12:20] ='Seahawks'
#must create new team name
new_team = team[:12]+'Beavers'
print(new_team) #prints New England Beavers
print(team) #still prints New England Patriots


#SEARCHING
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'a')) #finds a at index 8 beacuse it comes before index 13

#use for loop to search
for i in range(len(team)):
    if team[i] == 'a':
        print(i)
#prints index 8 and 13 where a is

for i, letter in enumerate(team):
    if letter == 'a':
        print(i, letter)
#prints index and value  8 a and 13 a


for i, letter in enumerate(team):
        print(i, letter)
#prints index and value 

#LOOPING AND COUNTING
# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
#counts # of letter a

#exercise 2
def count(s, letter):
    c = 0
    for each in s:
        if each == letter:
            c += 1
        return c

print(count(team, 'a')) #should be 2
print(count(team, ' ')) #should be 2


#STRING METHODS
#converts all letters to uppercase 
team = 'New England Patriots'
new_team = team.upper()
print(new_team)

#premade function for find
team = 'New England Patriots'
index = team.find('a')
print(index)

print(team.find('En'))

#KNOW HOW TO USE SPLIT AND STRIP
team.split()
team.split('e')
team.split('a')