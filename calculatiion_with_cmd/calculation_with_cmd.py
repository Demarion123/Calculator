print("Welcome to My calculator")
answer = input("Press any key to commence calculation.If you wish to quit click [q]. ").lower()
if answer == "q":
    print("Goodbye!")
    quit
else:
    print("Let's go")
    while True:
        a = int(input("input the first number: "))
        b = int(input("input the second number: "))
        choice = input("choose from addition,subtraction,multiplication and division[+,-,*,/]: ").lower()
        if choice == "+":
            print( a + b )
        elif choice == "-":
            print( a - b )
        elif choice == "/":
            print( a / b )
        else:
            print( a * b )    
