n = 5  

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

print()  

for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

