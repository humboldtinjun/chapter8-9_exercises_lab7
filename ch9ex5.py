# total length of strings
def total_length(word_list):
    """
    takes a list of words and gives the total length of all words joined.
    """
    total = 0  # starts total counter
    for word in word_list:
        total += len(word)  # add the length of each word
    return total  # Return total length

# 📌 load words from the text file
word_list = [line.strip() for line in open("text_doc.txt")]

# 📌 test the function
print("Total length of words:", total_length(word_list))
