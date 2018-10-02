fin = open('session09/words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1
# print(counter)
# #113809

def read_long_words():
    """
    prints only the words with more than 20 characters
    """
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

# print(read_long_words())


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    # for letter in word:
    #     #if letter == 'e' or letter == 'E':
    #     #if letter.lower() == 'e':
    #         return False
    # return True
    return not 'e' in word.lower()

#SOLUTION
# def has_no_e(word):
#     for letter in word:
#         if letter == 'e':
#             return False
#     return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('Epslon'))

#Modify your program from the previous section to print only the 
# words that have no “e” and compute the percentage of the words 
# in the list that have no “e”.
total_words = 113806

def has_no_e_calc(): 
    counter = 0
    for line in fin:
        word = line.strip()
        #if 'e' not in word:
            #print(word)
        if has_no_e(word):
            counter += 1

    print(counter)
    #print('{:.4f}% of words have no "e."'.format((counter/total_words))*100))

#has_no_e_calc()
#should be 33%

#print(has_no_e_calc())  

def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    return not forbidden in word

#SOLUTION
# def avoids(word, forbidden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True

# print(avoids('Babson', 'ab')) #False
# print(avoids('College', 'ab')) #True
# print(avoids('Bason', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    if available in word:
        return True
    else: 
        return False 

#SOLUTION
# def uses_only(word, available):
#     for letter in word: 
#         if letter not in available:
#             return False
#     return True

# print(uses_only('Babson', 'aBbsonxyz')) #False
# print(uses_only('college', 'aBbsonxyz')) #False


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    if required in word:
        return True
    else:
        return False

#SOLUTION
# def uses_all(word, required):
#     for letter in required: 
#         if letter not in word:
#             return False
#     return True

# def uses_all(word, required):
#     return uses_only(required, word)

# print(uses_all('Babson', 'abs')) #True
# print(uses_all('college', 'abs')) #False


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    # for lets in word:
    #     if lets.sort():
    #         return True
    #     else:
    #         return False

#SOLUTION
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


# print(is_abecedarian('abs')) #True
# print(is_abecedarian('college')) #False

#EXERCISE 2
#Rewrite is_abecedarian using recursion
def is_abecedarian_recursion(word):
    if word :
        return
    else: 
        return

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))

#Rewrite is_abecedarian using while loop.
def is_abecedarian_while(word):
    iteration = 0
    while iteration < len(word):
        previous = word[0]
        for c in word:
            if c < previous:
                return False
            previous = c
        return True

# print(is_abecedarian('abs')) #True
# print(is_abecedarian('college')) #False




#Try this after class, find 62 letters
def find_words_only_using_planet():
    fin = open('session09/words.txt')
    number_of_words_using_planet = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, 'planet'):
            print(word)
            number_of_words_using_planet += 1
    return number_of_words_using_planet


#print('Number of words using only letters from "planet":',
      #find_words_only_using_planet())

def uses_all2(word, required):
    return uses_only(required, word)

def uses_all_vowels():
    counter = 0
    for line in fin:
        word = line.strip()
        if uses_all2(word, 'aeiou'):
            counter += 1
    return counter

#print(uses_all_vowels())


def find_words_no_vowels():
    fin = open('session09/words.txt')
    counter_no_vowel = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if avoids(word, 'aeiouy'):
            print(word)
            counter_no_vowel += 1
    return counter_no_vowel/counter_total


print('The percentage of the words with vowel letters is {:.2f}%.'.format(
    find_words_no_vowels()*100))