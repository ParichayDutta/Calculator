def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please choose a valid operation.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The result is: {num1 + num2}")

            elif choice == 2:
                print(f"The result is: {num1 - num2}")

            elif choice == 3:
                print(f"The result is: {num1 * num2}")

            elif choice == 4:
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result is: {num1 / num2}")

            # Ask if the user wants to perform another calculation
            another = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")


calculator()
