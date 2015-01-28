print("Welcome to lowercaser!")
valid_d = False
while not valid_d:
    upper = input("Key in a phrase!")
    if not upper.isalpha():
        print("Letters only!")
    else:
        valid_d = True

print(" '{0}' ".format(upper.lower()))
