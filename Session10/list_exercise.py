def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for nested in t:
        total += sum(nested)
    return total

t = [[1, 2], [3], [4, 5, 6]]
# first = 3
# second = 3 + 3
# third = 6 + 15
# total = 21
nested_sum(t)

#dont change original list in for loop
def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3] input is list of numbers
    >>> cumsum(t) output is LIST
    [1, 3, 6]
    """
    total = 0
    res = [] #create new empty list
    for x in t:
        total += x #add next number in list
        res.append(total) #every iteration append current sum 
        # print('current list:')
        # print(res)
    return res
#replace each number in list with current sum

t = [1, 2, 3]
cumsum(t)
# first = 1, second 1+2 = 3, third 3+3 = 6
# output is list [1, 3, 6]



def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:-1] #this is a new list

t = [1, 2, 3, 4]
middle(t)


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    # del and pop work
    del t[0]
    del t[-1]
    # t.pop(0)
    # t.pop(-1)
    return None

t = [1, 2, 3, 4]
chop(t)
t


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    # before = t[0]
    # for c in t:
    #     if c < before:
    #         return False
    #     before = c
    # return True
    return t == sorted(t)

is_sorted([1, 2, 2])
is_sorted(['b', 'a'])

a = [745, 1, 2244, 4, 224, 34379]
sorted(a) #sorts 
a # not changed
a.sort() #nothing happens, sorts internally
a #a is changed


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    True
    """
    return sorted(word1) == sorted(word2)

is_anagram('stop', 'pots')
is_anagram('different', 'letters')
is_anagram([1, 2, 2], [2, 1, 2])


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    for i in s:
        if s.count(i) > i:
            return True
    return False

# print(has_duplicates('cba'))
# print(has_duplicates('abba'))


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

print(has_adjacent_duplicates('cba'))
print(has_adjacent_duplicates('abca'))
print(has_adjacent_duplicates('abbc'))


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    # print(nested_sum(t))

    # t = [1, 2, 3]
    # print(cumsum(t))

    # t = [1, 2, 3, 4]
    # print(middle(t))
    # chop(t)
    # print(t)

    # print(is_sorted([1, 2, 2]))
    # print(is_sorted(['b', 'a']))

    # print(is_anagram('stop', 'pots'))
    # print(is_anagram('different', 'letters'))
    # print(is_anagram([1, 2, 2], [2, 1, 2]))

    # print(has_duplicates('cba'))
    # print(has_duplicates('abba'))


if __name__ == '__main__':
    main()