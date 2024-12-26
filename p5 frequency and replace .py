def find_frequency(string, char):
    return string.count(char)

def replace_character(string, old_char, new_char):
    return string.replace(old_char, new_char)

def remove_first_occurrence(string, char):
    return string.replace(char, '', 1)

def remove_all_occurrences(string, char):
    return string.replace(char, '')

string = input("Enter a string: ")

char = input("Enter the character to find frequency: ")
print(f"Frequency of '{char}' in the string: {find_frequency(string, char)}")

old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
print(f"String after replacement: {replace_character(string, old_char, new_char)}")

char_to_remove = input("Enter the character to remove (first occurrence): ")
print(f"String after removing first occurrence: {remove_first_occurrence(string, char_to_remove)}")

char_to_remove_all = input("Enter the character to remove (all occurrences): ")
print(f"String after removing all occurrences: {remove_all_occurrences(string, char_to_remove_all)}")
