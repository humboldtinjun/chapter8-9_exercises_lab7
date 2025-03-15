def check_word(word, correct_position, misplaced_letters, forbidden_letters):
    """
    checks if a word could be the target wordle word.
    :param word: the word were checking
    :param correct_position: a dictionary {index: letter} for letters in the right spot
    :param misplaced_letters: a dictionary {letter: set(position) for letters in the word but in the wrong spot
    :param forbidden_letters: letters that cant be in the word
    :return:
    """
    # check letter position
    for index, letter in correct_position.items():
        if word[index] != letter:
            return False

    #check misplaced words
    for letter, bad_position in misplaced_letters.items():
        if letter not in word:
            return False
        for pos in bad_position:
            if word[pos] == letter:
                return False
    # check forbidden letters
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True #if all checks out the word will pass true

#testing the function
correct_positions = {4: 'E'}  # 'E' must be in position 4
misplaced_letters = {'R': {2}}  # 'R' must be in the word but NOT at position 2
forbidden_letters = {'T', 'I', 'D'} # 'T', 'I', and 'D' cannot appear in the word

#test words
word_list = ["MOWER", "EVERY", "THREE", "BREAD", "BELOW", "EMOTE", "MOTEL"]


# checks which words are possible
valid_words = [word for word in word_list if check_word(word, correct_positions, misplaced_letters, forbidden_letters)]

#print
print("Possible words:", valid_words)