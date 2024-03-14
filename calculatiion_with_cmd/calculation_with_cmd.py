
print("input numbers that will be calculated")

while True:
    a = int(input("input the first number: "))
    b = int(input("input the second number: "))
    choice = input("choose from addition,subtraction,multiplication and division[ +,-,*,/]: ")
    if choice == "+":
        print( a + b )
    elif choice == "-":
        print( a - b )
    elif choice == "/":
        print( a / b )
    else:
        print( a * b )
        continue
