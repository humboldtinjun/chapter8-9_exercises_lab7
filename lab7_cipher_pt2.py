def vigenere_header(alphabet):
    """Prints the header row"""
    print('|   ' + ' '.join(f"| {letter}" for letter in alphabet) + ' |')  #used join instead of for loop
    print(f"{'|---' * (len(alphabet) + 1)}|")


def vigenere_sq(alphabet):
    """Generates and prints the full Vigenère square by shifting them on each row"""
    alpha_len = len(alphabet)
    vigenere_header(alphabet)

    for shift in range(alpha_len):
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]  # Uses slicing
        print(f" {shifted_alphabet[0]}", end=' ')

        for letter in shifted_alphabet:
            print(f"| {letter}", end=' ')

        print("|")


def letter_to_index(letter, alphabet):
    """Returns the index of a given letter in the alphabet"""
    return alphabet.index(letter.upper())  # makes it case insensitivea


def index_to_letter(index, alphabet):
    """Returns the letter that matches the given index in the alphabet"""
    return alphabet[index] if 0 <= index < len(alphabet) else ''  # Prevents out-of-bounds errors


def vigenere_index(key_letter, plaintext_letter, alphabet):
    """Computes the Vigenère cipher index by shifting the letters by the key letter"""
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    """Encrypts the plaintext using the Vigenère cipher with the given key."""
    cipher_text = []  # Store result in a list instead of a string
    key_indexes = [letter_to_index(k, alphabet) for k in key]  # Precompute key indexes
    counter = 0

    for c in plaintext:
        if c == ' ':
            cipher_text.append(' ')  # save spaces
        elif c.upper() in alphabet:
            # Compute new index using the key
            new_index = (letter_to_index(c, alphabet) + key_indexes[counter % len(key)]) % len(alphabet)
            cipher_text.append(index_to_letter(new_index, alphabet))  # Append result to list
            counter += 1
        else:
            cipher_text.append(c)  # save non abc characters

    return "".join(cipher_text)  # change list to a string at the end


def decrypt_vigenere(key, ciphertext, alphabet):
    """Decrypts the ciphertext using the Vigenère cipher with the given key."""
    decrypted_text = []  # Store result in a list instead of a string
    key_indexes = [letter_to_index(k, alphabet) for k in key]  # precompute key indexes
    counter = 0

    for c in ciphertext:
        if c == ' ':
            decrypted_text.append(' ')  # preserve spaces
        elif c.upper() in alphabet:
            # compute original index by subtracting key index
            letter_index = letter_to_index(c.upper(), alphabet)
            new_index = (letter_index - key_indexes[counter % len(key)]) % len(alphabet)
            decrypted_letter = index_to_letter(new_index, alphabet)

            # saves original letter case
            if c.islower():
                decrypted_text.append(decrypted_letter.lower())
            else:
                decrypted_text.append(decrypted_letter)

            counter += 1  # increment for letters
        else:
            decrypted_text.append(c)  # changes non abc characters

    return "".join(decrypted_text)  # changes list to  string at the end


# global list to store encrypted messages
encrypted_messages = []

# define the encryption key and alphabet
key = 'BLUESMURF'
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# menu options stored as  list of lists
menu_options = [
    ("Encrypt", lambda: encrypted_messages.append(encrypt_vigenere(key, input("Enter plaintext: "), alphabet))),
    ("Decrypt", lambda: [print("Decrypted:", decrypt_vigenere(key, msg, alphabet)) for msg in encrypted_messages]),
    ("Dump Encrypted Text", lambda: print("Encrypted Messages:", encrypted_messages)),
    ("Quit", exit)
]

# menu Loop
while True:
    print("\nMenu:")
    for i, (option, _) in enumerate(menu_options, 1):
        print(f"{i}. {option}")

    choice = input("choose an option: ")
    if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
        menu_options[int(choice) - 1][1]()  # Calls the selected function
    else:
        print("wrong choice. enter a number between 1 and 4.")


#print(vigenere_index('b', 'h', alphabet))

#print(encrypt_vigenere(key, message, alphabet))





#vigenere_sq(alphabet)