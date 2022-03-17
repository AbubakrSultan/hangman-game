from answer_list import get_random_word


def get_masked_word(original_word, masked_word, character=None):
    positions = []
    for i in range(len(original_word)):
        for pos, char in enumerate(original_word):
            if char == character:
                positions.append(pos)

    new_word = ''
    p = 0
    for i in masked_word:
        if p in positions:
            new_word += character
        else:
            new_word += i
        p += 1

    return new_word


def give_answer():
    random_word = get_random_word()
    hidden_random_word = '_'*len(random_word)
    print("Here is the word to guess:   " + hidden_random_word)

    for r in range(len(random_word) * 3):
        if hidden_random_word == random_word:
            print('You Win!!! 🥳🥳🥳')
            return True
        guess = input("Choose a letter  ")
        guess = guess.lower()
        if len(guess) != 1:
            print('Make sure there is 1 letter.')
        else:
            if guess in random_word:
                hidden_random_word = get_masked_word(random_word, hidden_random_word, guess)
                print('Correct!')
            else:
                print('Incorrect! try again')
        print(hidden_random_word)
        print(str(len(random_word) * 3 - r) + " turns left! ⏲️️")
        print

    print('You Lose!!! ☹️☹️☹️')
    print('The correct answer is:   ' + random_word)
    return False


print("\nI challenge you to a game of hangman! 🤯🤯🤯\n")
give_answer()
