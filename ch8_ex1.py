# ask a virtual assistant
# What are the most common special characters used in python reg expressions?
### some of the most common are
#.	Matches any character except a newline
#^	Matches the start of a string
#$	Matches the end of a string
#*	Matches zero or more occurrences
#+	Matches one or more occurrences
#?	Matches zero or one occurrence
#\d	Matches any digit (0-9)
#\D	Matches anything that’s not a digit
#\w	Matches any word character (letters, digits, underscores)
#\W	Matches any non-word character
#\s	Matches any whitespace (spaces, tabs, newlines)
#\S	Matches any non-whitespace character
#{n}	Matches exactly n times
#{n,m}	Matches between n and m times
#[]	Matches any one of the characters inside
#()	Groups part of a pattern
###

# matches 10 dig phone number
#import re

#pattern = r'^\d{3}-\d{3}-\d{4}$'  # Three digits, hyphen, three digits, hyphen, four digits

#test_numbers = ["123-456-7890", "456-789-0123", "1234567890", "123-45-6789"]

#for number in test_numbers:
    if re.search(pattern, number):
        print(f"Valid phone number: {number}")
    else:
        print(f"Invalid phone number: {number}")
        pass
#match street address
#import re

#pattern = r'^\d+\s\w+\s(ST|AVE)$'

#test_addresses = ["123 Main ST", "456 Oak AVE", "789 Elm Rd", "100 Pine ST"]

#for address in test_addresses:
   # if re.search(pattern, address):
        print(f"Valid address: {address}")
   # else:
        print(f"Invalid address: {address}")
pass

#match full name
#import re

#pattern = r'^(Mr|Mrs|Dr)\.\s[A-Z][a-z]+(\s[A-Z][a-z]+)*$'

#test_names = ["Mr. John Smith", "Mrs. Emily Davis", "Dr. A. Strange", "Ms. Mary", "John Doe"]

for name in test_names:
    if re.search(pattern, name):
        print(f"Valid name: {name}")
    else:
        print(f"Invalid name: {name}")
pass
#match a legal url
import re

pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-z]{2,6}(/.*)?$'

test_urls = [
    "https://www.google.com",
    "http://example.org",
    "www.test-site.net",
    "invalid_url",
    "ftp://nothttp.com"
]

for url in test_urls:
    if re.search(pattern, url):
        print(f"Valid URL: {url}")
    else:
        print(f"Invalid URL: {url}")
