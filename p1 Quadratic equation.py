a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + discriminant**0.5) / (2 * a)
    x2 = (-b - discriminant**0.5) / (2 * a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    real_part = -b / (2 * a)
    imaginary_part = (-discriminant)**0.5 / (2 * a)
    print(f"x1 = {real_part} + {imaginary_part}i")
    print(f"x2 = {real_part} - {imaginary_part}i")

#the input 1 1 -2
