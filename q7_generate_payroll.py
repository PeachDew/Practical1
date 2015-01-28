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
