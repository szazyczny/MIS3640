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

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('Epslon'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letters in word:
        return not forbidden in word


print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    pass


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    pass


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))