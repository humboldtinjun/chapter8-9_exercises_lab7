def is_palindrome(word):
    """
    checks if a word is a palindrome.
    """
    return word.lower() == word.lower()[::-1]  # the -1 makes it check it in reverse


def find_palindromes(word_list):
    """
    finds all palindromes in a given word list.
    """
    return [word for word in word_list if len(word) >= 7 and is_palindrome(word)]
     #this only returns the word if its greater or equal to 7 and is a palindrome

# Load words from a file
word_list = [line.strip() for line in open("text_doc.txt")] #loads words into text_doc

# Find palindromes with at least 7 letters
palindromes = find_palindromes(word_list) #aliases find palindromes

# Print results
print("palindromes found:", palindromes)

# Test cases
print(is_palindrome("racecar"))  #  True
print(is_palindrome("rotator"))  # True
print(is_palindrome("banana"))   # False
print(is_palindrome("Noon"))     # True (ignores case)
