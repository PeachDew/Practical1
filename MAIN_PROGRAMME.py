#Practical 1

#Spacing

def space():
    print('''


    ''')

#Fareinheit Converter

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

space()

#Cylinder Volume calculator

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

space()

#Miles to Km converter

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

space()

#Interger digits calculator

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

space()

#Ascii

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

space()

#Lowercase-er

print("Welcome to lowercaser!")
valid_d = False
while not valid_d:
    upper = input("Key in a phrase!")
    if not upper.isalpha():
        print("Letters only!")
    else:
        valid_d = True

print(" '{0}' ".format(upper.lower()))

space()

#Payroll

print("Welcome to payroll generator!")
name = input("Key in your name!")
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
valid_e = False
while not valid_e:
    hours = input("Key in your working hours per week!")
    if hours.startswith('-') and hours[1:].isdigit():
        print("Please enter a positive number")
    elif not hours.isdigit():
        print("Please enter a number")
    else:
        valid_e = True
valid_f = False
while not valid_f:
    pay = input("Key in your hourly pay!")
    if pay.startswith('-') and pay[1:].isdigit():
        print("Please enter a positive number")
    if isFloat(pay):
        valid_f = True
    elif not pay.isdigit():
        print("Please enter a number")
    else:
        valid_f = True
valid_g = False
while not valid_g:
    cpf = input("Key in your CPF contribution rate!")
    if cpf.startswith('-') and cpf[1:].isdigit():
        print("Please enter a positive number")
    if isFloat(cpf):
        valid_g = True
    elif not cpf.isdigit():
        print("Please enter a number")
    elif int(cpf) > 100 or int(cpf) < 0:
        print("Number out of range. (1-100)")
    else:
        valid_g = True

gross = float(pay) * float(hours)
cpfamt = float(cpf) / 100 * float(gross)
net = float(gross) - float(cpfamt)

print('''
Payroll statement for {0}
Number of hours worked a week {1}
Hourly pay rate ${2}
Gross pay = ${3}
CPF contribution at {4}% = {5}
Net pay = {6} '''.format(name,hours,round(int(pay),2),round(int(gross),2),cpf,round(int(cpfamt),2),round(int(net),2)))

print("You've reached the end :) ")
import time
time.sleep(3)

print('''
  _    _                                                 _       _             _
 | |  | |                                               | |     | |           | |
 | |__| | __ ___   _____    __ _    __ _  ___   ___   __| |   __| | __ _ _   _| |
 |  __  |/ _` \ \ / / _ \  / _` |  / _` |/ _ \ / _ \ / _` |  / _` |/ _` | | | | |
 | |  | | (_| |\ V /  __/ | (_| | | (_| | (_) | (_) | (_| | | (_| | (_| | |_| |_|
 |_|  |_|\__,_| \_/ \___|  \__,_|  \__, |\___/ \___/ \__,_|  \__,_|\__,_|\__, (_)
                                    __/ |                                 __/ |
                                   |___/                                 |___/
''')


