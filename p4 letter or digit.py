def digit_to_text(digit):
    digit_names = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
        '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }
    return digit_names.get(digit, '')

char = input("Enter a character: ")

if char.isalpha():
    print("The character is a letter.")
    if char.isupper():
        print("The letter is uppercase.")
    else:
        print("The letter is lowercase.")
elif char.isdigit():
    print("The character is a numeric digit.")
    print(f"The digit name is: {digit_to_text(char)}")
else:
    print("The character is a special character.")
#the input number or letter like e or 3
