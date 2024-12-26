n = 5  # Number of rows for the pyramid

# Pyramid
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

print()  # Blank line between the pyramid and reverse pyramid

# Reverse Pyramid
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
