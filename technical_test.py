"""
Design a function that reverses the digits of an integer. For example, 50
should become 5 and -12 should become -21.
"""
def reverse_digits(num):

  # Convert the integer to a string
    str_n = str(abs(num))

  # Check if the number is negative
    is_negative = str_n[0] == '-'

 # Reverse the string
    reversed_str = str_n[::-1]

# for negative numbers, add the '-' sign to the reversed string
    if is_negative:
        reversed_str = '-' + reversed_str

  # Convert the reversed string back to an integer
    reversed_int = int(reversed_str)

    return reversed_int

# Call the function
print(reverse_digits(50))
print(reverse_digits(-12))

"""# ***2.***"""

# Write a recursive function to calculate the factorial of a number
# A recursive function calls itself. Using a formula in a function
def factorial (n):

  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))

"""# ***3.***"""

"""
Design a function that takes a string or sequence of characters as input and
returns the character that appears most frequently.
//Eg 11189 => '1'
//hello => l
"""
def frequent_char(input_string):
    # Initialize two lists
    characters = []
    frequencies = []

    # Loop every character in the string
    for char in input_string:
        if char in characters:
            # If the character is already in the list, increment its frequency
            index = characters.index(char)
            frequencies[index] += 1
        else:
           #Add new charaters to the list and set frequency is 1
            characters.append(char)
            frequencies.append(1)

    # Find the index of the maximum frequency
    max_index = frequencies.index(max(frequencies))

    # Return the character with the highest frequency
    return characters[max_index]

# Get input from the user
user_input = input("Enter a string or sequence of characters: ")

# Find the most frequent character
result = frequent_char(user_input)

# Print the result
print(f"The most frequent character is: {result}")

"""# ***4.***"""

"""
Design a function that determines whether a given string is a pangram. A
pangram is a sentence or phrase containing every letter of the alphabet at
least once. Punctuation and case are typically ignored. For example, the
string "The quick brown fox jumps over the lazy dog" is a pangram, while
"Hello, world!" is not.
"""
def pangram(sentence):
    # Define the alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    # Convert the input string to lowercase and create a set of characters
    sentence = sentence.lower()
    characters = set(sentence)

    # Check if all alphabet letters are in the set of characters
    return alphabet.issubset(characters)

#Function Calling
input_sentence = input("Enter a string: ")


if pangram(input_sentence):
    print(f'"{input_sentence}" is a pangram.')
else:
    print(f'"{input_sentence}" is not a pangram.')

# print(pangram("The quick brown fox jumps over the lazy dog"))
# print(pangram("Hello, world!"))

"""# ***5.***"""

"""
Design a function that takes a list of integers as input. The function should
return True if the list contains two consecutive threes (3 next to a 3) anywhere
within the list. Otherwise, it should return False. For example, the function
should return True for [1, 3, 3] and False for [1, 3, 1, 3].
"""
def two_threes(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False

# Call the function
print(two_threes([1, 3, 4, 3, 3]))
print(two_threes([1, 3, 1, 2]))

"""# ***6.***"""

"""
Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
for his unique way of speaking. He often reverses the order of words in his
sentences. For example, instead of saying "I am home" he might say "Home
am I" Design a function that takes a sentence as input and returns a new
sentence with the words reversed in the same order that Master Yoda would
use.
"""
def master_yoda(words):
    # Split the sentence into words
    words = words.split()

    reversed_words = words[::-1]
 # Join the reversed words back into a sentence
    return ' '.join(reversed_words)

#Input
input_sentence = input("Master Yoda said: ")

# Call the function
print(master_yoda(input_sentence))