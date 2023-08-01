# day6 Lecuture Morning..
# Advanced topic in python
# reqular expression..
# Generators and iterators
# Decorators
# Context managers
# Multithreading and multiprocessing

# SUMMARY..
"""\d: Matches any digit (0-9)
 \w: Matches any alphanumeric character (a-z,A-Z,0-9 and uderscore).
 \s:Matches any whitespace character(space,tab,newline).
 .: Matches any character except a newline.
 *: Matches zero or more occurancesof the preceding character or group.
 +: Matches one or more occurances of the preceding character or group.
 ?: Matches zero or more occurances of the preceding character  or group.
 []: Macthes any character within the square bracket.
 [^]: Matches any character not within the square bracket.
 ^: Matches the start of a line.
 $: Matches the end of a line.

"""

# EXAMPLES 
# MATCHING AND SEARCHING
# REGREX re.match(), re.search(), re.findall()
# example Demonstrating regex | Match  First word, Match Group WORD, Match all Numbers

import re
text = "What is your name ?, My name is samuel Wel"
match = re.search(r"\b\w+\b", text)
if match:
    print("Match:", match.group())
matches = re.findall(r"\d+", text)
print("Matches:",matches)

 # validting email

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
       return True
    else:
       return False 
email1 = "samuel777@gmail.com"
email2 = "samue@gmail.com"
print(validate_email(email1))
print(validate_email(email2))

 # Generators and iterators
 # yield generator
 # Iterator '_iter_' "_next_" iterator

def factorial(n):
    if n == 0:
        yield 1
    else:
        # yield n * factorial(n-1)
        fact = 1
        for i in range(1, n+1):
            fact *= i
        yield fact
for i in range (1, 10):
    print(factorial(i))

def squares():
    for i in range (1, 10):
        yield i ** 2

squares_iterator =  squares()
for i in range(5):
    print(next(squares_iterator))









