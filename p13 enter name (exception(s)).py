import re

class InvalidNameError(Exception):
    pass

def check_name(name):
    if re.search(r'[^a-zA-Z\s]', name):
        raise InvalidNameError("Name contains invalid characters. Only letters and spaces are allowed.")
    return name

try:
    name = input("Enter your name: ")
    check_name(name)
    print(f"Hello, {name}!")
except InvalidNameError as e:
    print(e)
