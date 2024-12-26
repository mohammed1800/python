input_list = [1, 2, 'hello', 4, 5, 6, 8, 9.5, 10]

cubes = [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

print(cubes)
