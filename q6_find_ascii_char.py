print("Welcome to ascii character finder!")
valid_c = False
while not valid_c:
    char = input("Key in a number between 0-127")
    if not char.isdigit():
        print("Please enter a positive integer.")
    elif int(char) > 128 or int(char) < 0:
        print("Number out of range")
    else:
        valid_c = True
print("Your character is '{0}' ".format(chr(int(char))))
