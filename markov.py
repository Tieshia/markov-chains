"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as origin_text:
        raw_text = origin_text.read()

    return raw_text


def make_chains(text_string):
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
    for i in range(len(words) - 1):
        # create tuple for word[i] and word[i +1]
        new_key = (words[i], words[i + 1])
        if (i + 2) < len(words):
            new_val = words[i + 2]
        else:
            new_val = None

        # add as key to chains dictionary
        if chains.get(new_key) is None:
            chains[new_key] = [new_val]
        else:
            chains[new_key].append(new_val)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # choose random key, cast tuple as list
    first_key = list(choice(chains.keys()))

    words.extend(first_key)

    # while loop until value == None

    test_key = tuple(first_key)

    while chains[test_key] != [None]:
        new_word = choice(chains[test_key])

        # append a random value from chains[key] to words[]
        words.append(new_word)

        # key = words[-2, -1]
        test_key = (words[-2], words[-1])


    # convert list to string

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# print input_text

# Get a Markov chain
chains = make_chains(input_text)

# print chains
# Produce random text
random_text = make_text(chains)

print random_text
