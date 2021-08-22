#! /usr/bin/env python3

num1 = int(input('Enter a number: '))
operator = input('Enter an operator: ')
num2 = int(input('Enter another number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)


