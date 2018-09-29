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
def has_no_e_calc(): 
    for line in fin:
        word = line.strip()
        if 'e' not in word:
            print(word)

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