# multi purpose calculator

# money calculator
def money():
    money = int(input('Enter number of cents: '))
    quarters = money // 25
    money = money % 25
    dimes = money // 10
    money = money % 10
    nickels = money // 5
    money = money % 5
    cents =  money // 1
    print('You have',quarters,'quaters' )
    print('You have',dimes,'dimes')
    print('You have',nickels,'nickels')
    print('You have',cents,'pennies')

# time calculator
def time():
    time = int(input('Please enter the time in seconds: '))
    hours = time // 3600
    time =  time % 3600
    minutes = time // 60
    time =  time % 60
    seconds = time
    print(hours, 'h:', minutes, 'm:', seconds, 's')

# basic calculator
def basic():
    num1 = int(input('Enter number 1: '))
    operator = input('enter operator: ')
    num2 = int(input('Enter number 2: '))
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

# temperature converter
def temperature():
    cel = input('Start with celsius or fahrenheit: ')
    if cel == 'celsius':
        sius = float(input('enter temperature: '))
        print('In fahrenheit the temperature is',sius/5.0*9.0+32)
    if cel == 'fahrenheit':
        heit = float(input('enter temperature: '))
        print('In celsius the temperature is', heit - 32 *5/9)

def main():
    calculator = input("choose your calculator: money, time, basic, or temperature: ")
    if calculator == 'money':
        money()
    if calculator == 'time':
        time()
    if calculator == 'basic':
        basic()
    if calculator == 'temperature':
        temperature()


if __name__ == '__main__':
    main()




