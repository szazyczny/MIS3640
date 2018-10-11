#ITERATIONS

#LOOP
#print(1+2+3)

#iteration for sum 1-10
#need a variable to hold the sum value
# result = 0
# #for x in ... is to take every element into variable x, ane then execute the following block.
# for i in range(10): 
#     print(i+1)
#     result = result + i + 1
# print(result)

# result = 0 
# for i in range(10): 
#     print('current number to be added:', i+1)
#     result = result + i + 1
#     print('new result after this iteration', result)
# print('the final result:', result)

result = 0 
for i in range(1, 11): 
    #print('current number to be added:', i)
    result = result + i
    #print('new result after this iteration', result)
print('the final result:', result)

#sum 1 to 1000
result = 0 
for i in range(1, 1001): 
    #print('current number to be added:', i)
    result = result + i
    #print('new result after this iteration', result)
print('the final result:', result)

#identifying odd or even
for i in range(1, 11): 
    if i % 2 == 0:
        print(i, 'is an even number')
    else:
        print(i, 'is an odd number')


#calculate sum 1 to 1000 odd numbers only
result = 0
for i in range(1, 1001): 
    if i % 2 == 1:              #gives odd numbers
       result = result + i
print('the sum of odd numbers is:', result)

result = 0
for i in range(1, 1001, 2):         #gives odd numbers
    if i % 2 == 1:
       result = result + i
print('the sum of odd numbers is:', result)


#factorial of number 10 because multiplication
result = 1 
for i in range(1, 11): 
    result = result * i
print('the factorial of 10 is:', result)

#WHILE LOOP
#while something is true execute the block below and repeat until not true, if not true then skip and do next block
import time
def countdown(n):
    while n > 0:
        print(n)
        #time.sleep(1)       #means 1 second delay
        n = n - 1
    print('BLASTOFF!')
countdown(5)


counter = 0
while counter < 10:
    print(r"Here's Johnny!")
    counter = counter + 1   #if accidentally put -1 then it will print forever
    #same as counter += 1 

a = 1
a += 1
print(a)
#a = 2
a *= 10
print(a)
#a = 20
a /= 5
print(a)
#a = 4


message = 'Pranjal' #7 characters
for letter in message:  #letter is a temporary name for each character, can be any variable name
    print(letter)


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world":   #12 characters
        count += 1                  #counts characters in message = 12
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1                  
#iteration 0 count 12
#iteration 1 count 24
#iteration 2 count 36
#iteration 3 count 48
#iteration 4 count 60
#each iteration counts the characters again, keep running again 4x

#each iteration count is reset to 0 so it each iteratoin will return 12
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#with break
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:  #if iteration is even
            break               #means jump out of loop and stop current loop
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
#if true then prints (1), if false then prints full because doesnt break (12)
#iteration 0 count 1
#iteration 1 count 12
#iteration 2 count 1
#iteration 3 count 12
#iteration 4 count 1

#BREAK
while True:                 #keep running until user inputs done
    line = input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:   
    print('press q to quit')              
    line = input('>')
    if line == 'q':
        break
    print(line)
print('Done!')

mysum = 0
for i in range(5, 11, 2): #from 5-10 adding 2 each time
    mysum += i
    if mysum == 5:
        break
print(mysum)
#0+5 = 5 so it will print mysum
