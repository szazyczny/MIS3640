#DICTIONARIES

#Exercise 1
#Rewrite function histrogram using get. 
#You should be able to eliminate the if statement.
def histogramif(s):
    d = dict()          #empty dictionary
    for letter in s:         #for letter in string
        if letter not in d:  #if letter is not in the keys of dictionary
            d[letter] = 1    #dictionary value for that letter = 1
        else:           #if key exists in in dictionary
            d[letter] += 1   #add 1 to its value 
    return d            #returns each key and its value


hif = histogramif('Bookkeeper') 
print(hif)
# {'B': 1, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1}


def histogram(s):
    d = dict()
    for letter in s:
       d[letter] = d.get(letter, 0) + 1
    return d

h = histogram('Bookkeeper') 
print(h)
#{'B': 1, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1}


# number_of_e = h.get('e', 0)
# number_of_a = h.get('a', 0)
# print(number_of_e)
# print(number_of_a)




