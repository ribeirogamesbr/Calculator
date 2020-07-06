Calculator = True
while Calculator:
    print("1. Addittion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    cmd = int(input('Enter your choice'))
    if cmd == 1:
        print("Addition")
        First =int (input ("Enter first number"))
        Second =int (input("Enter second Number"))
        Result = First + Second
        print(First, '+' ,Second , '=' ,Result)
    elif cmd == 2:
        print("Subtraction")
        First =int (input("Enter first number"))
        Second (input ("Enter second number"))
        Result = First - Second
        print(First, '-' ,Second , '=' ,Result)
    elif cmd == 3:
        print("Multiplication")
        First = int (input("Enter first number"))
        Second = int (input("Enter second number"))
        Result = First * Second
        print(First, '*' ,Second ,'=' ,Result)
    elif cmd == 4:
        print('Division')
        First = int (input("Enter first number"))
        Second = int (input("Enter second number"))
        Result = First / Second
        print (First, "/" ,Second ,"=" ,Result)