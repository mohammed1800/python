t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a) Print half the values of the tuple in one line and the other half in the next line
half = len(t1) // 2
print(t1[:half])
print(t1[half:])

# b) Print another tuple whose values are even numbers in the given tuple
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print(even_tuple)

# c) Concatenate a tuple t2=(11,13,15) with t1
t2 = (11, 13, 15)
concatenated_tuple = t1 + t2
print(concatenated_tuple)

# d) Return maximum and minimum value from this tuple
max_value = max(concatenated_tuple)
min_value = min(concatenated_tuple)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
