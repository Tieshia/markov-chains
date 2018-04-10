"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as origin_text:
        raw_text = origin_text.read()

    return raw_text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # created tokenized list of words
    words = text_string.split()
    # iterate through first through second to last word
    for i in range(len(words) - (n-1)):
        # create tuple for word[i] and word[i +1]
        new_key = tuple(words[i: (i + n)])
        if (i + n) < len(words):
            new_val = words[i + n]
        else:
            new_val = None

        # add as key to chains dictionary
        if chains.get(new_key) is None:
            chains[new_key] = [new_val]
        else:
            chains[new_key].append(new_val)

    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    # choose random key, cast tuple as list
    words = list(choice(chains.keys()))

    # while loop until value == None

    test_key = tuple(words)

    while chains[test_key] != [None]:
        new_word = choice(chains[test_key])

        # append a random value from chains[key] to words[]
        words.append(new_word)

        # key = words[-2, -1]
        test_key = tuple(words[-n:])


    # convert list to string

    return " ".join(words)


input_path = sys.argv[1]

def run_all_functions(file_path, n):
    input_text = open_and_read_file(file_path)

    chains = make_chains(input_text, n)

    return make_text(chains, n)


random_text = run_all_functions(input_path, 3)

print random_text

# Open the file and turn it into one long string

# print input_text

# Get a Markov chain

#print chains
# Produce random text



