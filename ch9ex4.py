#reverse a sentence
def reverse_sentence(sentence):
    """
    reverses the order of words in a sentence
    """
    words = sentence.split()  # splits sentence into words
    words.reverse()  # reverse the list of words

    # capitalize first word and lowercase the rest
    words[0] = words[0].capitalize()  #capitlizes the letter in the 0 index of the word
    for i in range(1, len(words)): # for loop starts at 1 and goes to the length of the word
        words[i] = words[i].lower() # makes every letter in i lowercase

    return " ".join(words)  # join words back into a sentence


# test Cases
print(reverse_sentence("Reverse this sentence"))  # ➝ "Sentence this reverse"
print(reverse_sentence("Python is fun"))  # ➝ "Fun is python"
print(reverse_sentence("HELLO world"))  # ➝ "World hello"
print(reverse_sentence("Keep it simple"))  # ➝ "Simple it keep"
