# 1
sentence = input("Enter a short sentence: ").upper()
print(sentence)

# 2
paragraph = input("Enter a paragraph: ")
# split the paragraph into words
words = paragraph.split()
# count the number of words
word_count = len(words)
print(f"The paragraph has {word_count} words.")

# 3
string = input("Enter a string: ")
# checks if the string is digits (1234)
is_all_digits = string.isdigit()
print(f"All characters are digits: {is_all_digits}")

# 4
new_string = input("Please enter another string: ")
new_string_replace = new_string.replace('a', 'o')
print(new_string_replace)

# 5
full_name = input("Enter your full name: ")
name_parts = full_name.split()
initials = ''.join([part[0].upper() for part in name_parts])
print(f"Your initials are {initials}")

# 6
last_string = input("Please enter another string: ")
last_string_count = len(last_string)
print(f"The length of your string is: {last_string_count}")
