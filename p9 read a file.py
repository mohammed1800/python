def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    return content

def count_characters_words_lines(file_content):
    char_count = 0
    word_count = 0
    line_count = len(file_content)
    for line in file_content:
        char_count += len(line)
        word_count += len(line.split())
    return char_count, word_count, line_count

def character_frequency(file_content):
    freq = {}
    for line in file_content:
        for char in line:
            if char.isalnum():  
                freq[char] = freq.get(char, 0) + 1
    return freq

def reverse_words(file_content):
    words = ' '.join(file_content).split()
    return ' '.join(words[::-1])

def copy_lines(file_content):
    with open('File1', 'w') as file1, open('File2', 'w') as file2:
        for i, line in enumerate(file_content):
            if i % 2 == 0:  
                file1.write(line)
            else:
                file2.write(line)

file_name = input("Enter the file name: ")
file_content = read_file(file_name)

char_count, word_count, line_count = count_characters_words_lines(file_content)
print(f"Total characters: {char_count}")
print(f"Total words: {word_count}")
print(f"Total lines: {line_count}")

char_freq = character_frequency(file_content)
print("Character frequencies:")
for char, count in char_freq.items():
    print(f"'{char}': {count}")

reversed_words = reverse_words(file_content)
print(f"Words in reverse order: {reversed_words}")

copy_lines(file_content)
print("Even lines copied to 'File1' and odd lines copied to 'File2'.")
