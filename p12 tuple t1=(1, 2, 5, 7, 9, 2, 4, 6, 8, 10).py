t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

half = len(t1) // 2
print(t1[:half])
print(t1[half:])

even_tuple = tuple(x for x in t1 if x % 2 == 0)
print(even_tuple)

t2 = (11, 13, 15)
concatenated_tuple = t1 + t2
print(concatenated_tuple)

max_value = max(concatenated_tuple)
min_value = min(concatenated_tuple)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
