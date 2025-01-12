def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        # Get numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

