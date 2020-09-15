#multi purpose calculator

#money calculator
money = int(input('Enter number of cents:'))

quarters = money // 25
money = money % 25

dimes = money // 10
money = money % 10

nickels = money // 5
money = money % 5

cents =  money // 1

print('Quarters:',quarters)
print('Dimes:',dimes)
print('Nickels:',nickels)
print('Cents:',cents)

#time calculator
time = int(input('Please enter the time in seconds:'))

hours = time // 3600
time =  time % 3600
minutes = time // 60
time =  time % 60
seconds = time


print(hours, 'h:', minutes, 'm:', seconds, 's')

#basic calculator
num1 = int(input('Enter number 1:'))
operator = input('enter operator:')
num2 = int(input('Enter number 2:'))

if operator == '+':
    print(num1 + num2)
if operator == '-':
    print(num1 - num2)
if operator == '*':
    print(num1 * num2)
if operator == '/':
    print(num1 / num2)
if operator == '%':
    print(num1 % num2)
if operator == '//':
    print(num1 // num2)
if operator == '**':
    print(num1 ** num2)

