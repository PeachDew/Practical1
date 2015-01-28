print("Welcome to Cylinder Volume calculator!")
valid_y = False
while not valid_y:
    rad = input("Key in radius of base circle")
    if rad.startswith('-') and rad[1:].isdigit():
        print("Please enter a positive number")
    elif not rad.isdigit():
        print("Please enter a number")
    else:
        valid_y = True
valid_z = False
while not valid_z:
    height = input("Key in radius of base circle")
    if height.startswith('-') and height[1:].isdigit():
        print("Please enter a positive number")
    elif not height.isdigit():
        print("Please enter a number")
    else:
        valid_z = True

import math
basearea = pow(int(rad),2) * math.pi
cylvol = float(basearea) * float(height)

print("Volume of cylinder = {0:.3f} (3 d.p.)".format(cylvol))
