import random

# word_list = [
#     'hello', 'cool', 'sunny', 'sleeping', 'sleepy', 'incredible', 'word', 'awesome', 'bye', 'know'
# ]

word_file = "wordlist.10000"
word_list = open(word_file).read().splitlines()


def get_random_word():
    x = random.randint(0, len(word_list))
    word = word_list[x]
    return word
