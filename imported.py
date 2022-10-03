from classes import Operations

num1 = int(input('Enter the first number: '))
op = input('\nEnter an operator of your choice which can be any of the given: (+,-,*,/,%): ')
num2 = int(input('\nEnter your second number: '))

classes = Operations(num1=num1, num2=num2)


def user():
    if op == '+':
        return 'The sum of your numbers is: ' + str(classes.add())
    elif op == '-':
        return 'The result of the subtraction is: ' + str(classes.subtraction())
    elif op == '*':
        return 'The product of your numbers is: ' + str(classes.multiplication())
    elif op == '/':
        return 'The result of the division is: ' + str(classes.division())
    elif op == '%':
        return 'The remainder of the numbers is: ' + str(classes.modulo())

    else:
        return op+' is a wrong Operator!! Try again!!'


print(user())
