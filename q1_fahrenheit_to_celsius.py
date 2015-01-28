print("Welcome to Fareinheit to Degree converter!")
valid_x = False
while not valid_x:
    fheit = input("Key in temperature in fareinheit:")
    if fheit.startswith('-') and fheit[1:].isdigit():
        valid_x = True
    elif not fheit.isdigit():
        print("Please enter a number.")
    else:
        valid_x = True
print("Temperature in Fareinheit=", fheit)
degree = (float(fheit) - 32) / 1.8
print("Temperature in Degree= {0: .3f} (3dp)".format(degree))
