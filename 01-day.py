print("""

01 ---> addition
02 ---> substraction
03 ---> multiplication
04 ---> division

""")

print("Select one of the actions: ")
transaction = int(input())
print("Enter the first number: ")
first_number = int(input())
print("Enter the second number: ")
second_number = int(input())

def add():
    addition = first_number + second_number
    print("Transaction result:")
    print(addition)

def sub():
    substraction = first_number - second_number
    print("Transaction result:")
    print(substraction)

def multip():
    multiplication = first_number * second_number
    print("Transaction result:")
    print(multiplication)

def div():
    division = first_number/second_number
    print("Transaction result:")
    print(division)


if transaction == 1:
    add()
elif transaction == 2:
    sub()
elif transaction == 3:
    multip()
elif transaction == 4:
    div()
else:
    print("You chose the wrong number!")



