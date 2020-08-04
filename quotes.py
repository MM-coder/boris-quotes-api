import random

def get_random_quote():

    # Open the file that contains the quotes

    with open('quotes.txt', 'r') as f:

        # Using the readlines() function get a iterable
        # We then use the random.choice() function to get 
        # a random string from the iterable
        # We do the replace, to remove linebreaks

        return random.choice(f.readlines()).replace('\n', '')