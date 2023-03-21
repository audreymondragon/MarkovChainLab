"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    #create an empty dictionary
    chains = {}

    #split our long string into a words list
    words = text_string.split()

    #iterate through the list of words
    for i in range(len(words) - 2):
        #our keys will be bigram tuples
        key = (words[i], words[i + 1])
        #our values will be the word directly after each bigram
        value = words[i + 2]
        
        #if the key is not already in the dictionary, create an empty list as the value
        if key not in chains:
            chains[key] = []
        
        #append the value to the list we made in line 57 for its unique keys
        chains[key].append(value) 

    return chains


def make_text(chains):
    """Return text from chains."""

    #getting a random tuple from our dictionary as a start link
    current_key = choice(list(chains.keys()))
    words = []
    #adding the two words in the tuple to our words list
    words.extend(current_key)

    #continue to loop only if the current key is found in our dictionary
    while current_key in chains:
        #get the next word from the words associated with our key
        next_word = choice(chains[current_key])
        #add the chosen word to our words list
        words.append(next_word)
        #create a new key based off the chosen word
        new_key = (current_key[1], next_word)
        #reset the variables in the loop
        current_key = new_key

    
    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
