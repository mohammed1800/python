def swap_first_n_chars(str1, str2, n):
    return str2[:n] + str1[n:], str1[:n] + str2[n:]

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap: "))

new_str1, new_str2 = swap_first_n_chars(str1, str2, n)

print(f"Modified first string: {new_str1}")
print(f"Modified second string: {new_str2}")
