def vigenere_header(alphabet):
    """Prints the header row"""
    print('|   ' + ' '.join(f"| {letter}" for letter in alphabet) + ' |') #took out for loop used join
    print(f"{'|---' * (len(alphabet) + 1)}|")


def vigenere_sq(alphabet):
    """ generates and prints the full vigenere square by shifting them on each row"""
    alpha_len = len(alphabet)
    vigenere_header(alphabet)

    for shift in range(alpha_len):
        shifted_alphabet = alphabet[shift:] + alphabet[:shift] #uses slicing
        print(f" {shifted_alphabet[0]}", end=' ')

        for letter in shifted_alphabet:
            print(f"| {letter}", end=' ')

        print("|")

def letter_to_index(letter, alphabet):
    """Returns the index of a given letter in the alphabet"""
    return alphabet.index(letter.upper())  # changed it to change the letter were looking up to upper, not the alphabet


def index_to_letter(index, alphabet):
    """Returns the letter that matches the given index in the alphabet"""
    return alphabet[index] if 0 <= index < len(alphabet) else ''
#changed this one to only do what its supposed to nothing else making it faster.


def vigenere_index(key_letter, plaintext_letter, alphabet):
    """computes the vigenere cipher index by shifting the letters by the key letter"""
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    """encrypts the plaintext using the cipher w/ given key"""
    cipher_text = ''
    key_indexes = [letter_to_index(k, alphabet) for k in key]  # precompute key indexes
    counter = 0

    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            # use precomputed key index
            new_index = (letter_to_index(c, alphabet) + key_indexes[counter % len(key)]) % len(alphabet)
            cipher_text += index_to_letter(new_index, alphabet)
            counter += 1
    return cipher_text

def decrypt_vigenere(key, ciphertext, alphabet):
    """Decrypts the ciphertext using the Vigenère cipher with the given key."""
    decrypted_text = ''
    key_indexes = [letter_to_index(k, alphabet) for k in key]  # Precompute key indexes
    counter = 0

    for c in ciphertext:
        if c == ' ':
            decrypted_text += ' '  # keep spaces
        elif c.upper() in alphabet:
            # subtract key index instead of adding
            letter_index = letter_to_index(c.upper(), alphabet)  # ensure uppercase lookup
            new_index = (letter_index - key_indexes[counter % len(key)]) % len(alphabet)
            decrypted_letter = index_to_letter(new_index, alphabet)

            # preserve original casing uppercase stays uppercase, lowercase stays lowercase
            if c.islower():
                decrypted_text += decrypted_letter.lower()
            else:
                decrypted_text += decrypted_letter

            counter += 1  # only increment for letters
        else:
            decrypted_text += c  # saves non-alphabet characters

    return decrypted_text



key = 'BLUESMURF'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = 'Hello World, I am here'

encrypted_msg = encrypt_vigenere(key, message, alphabet)
print("Encrypted:", encrypted_msg)

decrypted_msg = decrypt_vigenere(key, encrypted_msg, alphabet)
print("Decrypted:", decrypted_msg)

print(letter_to_index('H', alphabet))  # Should return 7
print(letter_to_index('h', alphabet))  # Should ALSO return 7


print(index_to_letter(7, alphabet))  # Should print 'H'
print(index_to_letter(25, alphabet)) # Should print 'Z'
print(index_to_letter(26, alphabet)) # Should print '' (empty string, out of bounds)

#print(vigenere_index('b', 'h', alphabet))

#print(encrypt_vigenere(key, message, alphabet))





#vigenere_sq(alphabet)