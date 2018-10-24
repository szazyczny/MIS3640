#use encoding and make sure file path is correct

import random
import string

# steps to process file
# open file
# tokenize file - break doc to lines to words, clean up puncuation, convert to lower case, remove strange characters

# EXERCISE 1
# Modify function process_file to read a file, break each line into words,
# strip whitespace and punctuation from the words, and convert them to lowercase.
# strip, replace and translate
def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {} # key is word, value is frequency of word
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippable = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        for word in line.split():
            word = word.strip(strippable)
            word = word.lower()

            # if word in hist:
            #     hist[word] += 1
            # else:
            #     hist[word] = 1

            hist[word] = hist.get(word, 0) + 1
            
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

# EXERCISE 2
# Then modify total_words to count the total number of words in the book,
# number of times each word is used.

# Then modify different_words to print the number of different words
# used in the book. Compare different books by different authors, 
# written in different eras. Which author uses the most extensive 
# vocabulary?
def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist) # length of dictionary gives the number of unique keys


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = [] # new list
    for key, value in hist.items():
        t.append((value, key))
    
    t.sort
    t.reverse
    return t

def most_common_nostop(hist, excludestopwords=True):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    stopwords = process_file("session13/stopwords.txt", False)

    t = [] 
    for key, value in hist.items():
        if key not in stopwords:
            t.append((value, key))
    
    t.sort
    t.reverse
    return t

    # for word in h:
    #     h[word] = h.get(word, 0) + 1
    # return h

    # for freq, word in sorted(hist.items()):
    # return (freq, word)

    # for word in sorted(hist.items()):
    #     freq = hist.get(0, word) + 1
    # return freq

def print_most_common(hist, num=10): #10 is default value for num, it is optional to input a num arguement
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]: #find top "this many (num)" in the list
        print(word, '\t', freq)
#most common are stopwords like "the" and "i"



def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

    # dictionary = {}
    # for key in dictionary:
    #     if key in d1:
    #         if key in d2:
    #             return dictionary
    #         else:
    #             break

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    # probability = word/frequency 
    pass
    


def main():
    hist = process_file('session13/Pride and Prejudice.txt', skip_header=True)
    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

        words = process_file('words.txt', skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()