import re

def contains_pale_variants(line):
    """
    Checks if a line contains a word related to 'pale' or 'pallor'.
    Avoids matching words like 'impale'.
    """
    pattern = r'\b(pale|pales|paled|paleness|pallor)\b'
    return bool(re.search(pattern, line, re.IGNORECASE))  # case insensitive search

def count_pale_lines(file_path):
    """
    Reads a file and counts the number of lines containing 'pale' variations.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            count = 0
            for line in file:
                if contains_pale_variants(line.strip()):
                    print(line.strip())  # Print matching lines
                    count += 1

        print(f"\nTotal lines containing 'pale' variants: {count}")

    except FileNotFoundError:
        print(f"error: The file '{file_path}' was not found. Make sure it's in the correct directory.")

if __name__ == '__main__':
    file_path = 'files/TheCountofMonteCristo.txt'  # adjust path if needed
    count_pale_lines(file_path)
