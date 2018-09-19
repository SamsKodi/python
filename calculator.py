def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("I can't divide by zero. So I'm Returning zero.")
        return 0


def main():
    num1 = int(input("What number is 1?: "))
    num2 = int(input("What number is 2?: "))
    operation = input("What do you want to do?('add', 'subtract', 'multiply', and 'divide'?)Enter operation: ")
    if operation == 'add':
        print (add(num1, num2))
    elif operation == 'subtract':
        print (sub(num1, num2))
    elif operation == 'multiply':
        print(mul(num1, num2))
    elif operation == 'divide':
        print(div(num1, num2))
    else:
        print ('Listen up you big stupid, you think your funny doing it wrong?! Try AGAIN!')
    print ('Have A Good Day!')
    print ('CODED BY SAM TALIA (c)')

    user_yn = input('To quit type exit: ')
    if(user_yn !='exit'):
        exit()


main()
