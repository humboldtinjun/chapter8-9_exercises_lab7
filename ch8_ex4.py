import re

def check_word(word, correct_positions, misplaced_letters, forbidden_letters):
    """
    Checks if a word could be the target Wordle word.
    :param word: The word we're checking.
    :param correct_positions: A dictionary {index: letter} for letters in the correct spot.
    :param misplaced_letters: A dictionary {letter: set(positions)} for letters in the word but in the wrong spot.
    :param forbidden_letters: A set of letters that cannot be in the word.
    :return: True if the word is a valid possibility, False otherwise.
    """
    word = word.upper()  # normalize case

    # check if letters in correct positions match
    for index, letter in correct_positions.items():
        if word[index] != letter:
            return False

    # check misplaced letters, in word but NOT in the given positions
    for letter, bad_positions in misplaced_letters.items():
        if letter not in word:
            return False
        for pos in bad_positions:
            if word[pos] == letter:
                return False  # letter is in a wrong spot

    # check forbidden letters NOT in the word
    if any(letter in word for letter in forbidden_letters):
        return False

    return True  # if all checks pass, return True


# updated clues after guessing "TOTEM"
correct_positions = {4: 'M'}  # 'M' must be in position 4
misplaced_letters = {
    'E': {3, 4},  # 'E' is in the word, but NOT in position 3 or 4
    'R': {2}      # 'R' is in the word but NOT at position 2
}
forbidden_letters = {'T', 'I', 'D'}  # 'T', 'I', and 'D' cannot appear in the word

# test words
word_list = ["MOWER", "EVERY", "THREE", "BREAD", "BELOW", "EMOTE", "MOTEL"]


valid_words = [word for word in word_list if check_word(word, correct_positions, misplaced_letters, forbidden_letters)]
invalid_words = [word for word in word_list if word not in valid_words]

# print
print("possible words after 'TOTEM':", valid_words)
print("eliminated words:", invalid_words)
