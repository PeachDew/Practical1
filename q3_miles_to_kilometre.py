print("Welcome to Miles to kilometres converter!")
valid_a = False
while not valid_a:
    miles = input("Key in distance in miles")
    if miles.startswith('-') and miles[1:].isdigit():
        print("Please enter a positive number")
    elif not miles.isdigit():
        print("Please enter a number")
    else:
        valid_a = True

kilom = float(miles) * 1.60934
print("Distance in kilometers = {0:.3f} (3 d.p.)".format(kilom))
