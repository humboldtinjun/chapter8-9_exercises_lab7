# check if word is an anagram
def is_anagram(word1, word2):
    """
    checks if two words are anagrams
    """
    return sorted(word1.lower()) == sorted(word2.lower())

def find_anagrams(target_word, word_list):
    """
    finds all anagrams of the target word in a given word list
    """
    return [word for word in word_list if is_anagram(target_word, word)]
#load words from a file
word_list = [line.strip() for line in open("text_doc.txt")]

#find anagrams of "takes"
anagrams_of_takes = find_anagrams("takes", word_list)
#test cases
print(f"anagrams of 'takes': {anagrams_of_takes}")
print(is_anagram("listen", "silent")) #true
print(is_anagram("hello", "world")) #false
print(is_anagram("takes", "skate")) #true