print("Welcome to integer digits calculator!")
valid_b = False
while not valid_b:
    digits = input("Key in a number between 1-1000")
    if digits.startswith('-') and digits[1:].isdigit():
        print("Please enter a positive number")
    elif not digits.isdigit():
        print("Please enter a number")
    elif int(digits) > 1000 or int(digits) < 1:
        print("Number out of range")
    else:
        valid_b = True
if len(digits) == 3:
    print("Sum of digits =", int(digits[0])+int(digits[1])+int(digits[2]))
if len(digits) == 2:
    print("Sum of digits =", int(digits[0])+int(digits[1]))
if len(digits) == 1:
    print("Sum of digits =", digits)
