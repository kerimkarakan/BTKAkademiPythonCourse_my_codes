try:
     number1 = float(input("Enter first number for calculation: "))
     number2 = float(input("Enter second number for calculation: "))
except ValueError:
    print("Please enter a number!")
    exit()

def addition():
    add = number1 + number2
    if add.is_integer:
        add = int(add)
    print(add)

def substraction():
    substract = number1 - number2
    if substract.is_integer:
        substract = int(substract)
    print(substract)

def division():
    global divide
    if number2 == 0:
        print("Error! Division by zero!")
        divide = None
    else:
        divide = number1 / number2

def multiplication():
    multiply = number1 * number2
    if multiply.is_integer:
        multiply = int(multiply)
    print(multiply)

answer = int(input("Press 1 for addition, 2 for substraction, 3 for division, 4 for multiplication: "))

if answer == 1:
    addition()
elif answer == 2:
    substraction()
elif answer == 3:
    division()
    if divide is not None:
        print(divide)
elif answer == 4:
    multiplication()
else:
    print("Please enter a valid input!")







