def find_occurrences(str1, str2):
    indices = []
    index = str1.find(str2)
    while index != -1:
        indices.append(index)
        index = str1.find(str2, index + 1)
    return indices if indices else -1

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = find_occurrences(str1, str2)
print(result)

#the input:
#hihihi
#hi
