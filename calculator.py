# addition
def add(x, y):
    return x + y

# subtraction
def subtract(x, y):
    return x - y
# multiply
def multiply(x, y):
    return x * y

# division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display calculation history
def display_history(history):
    if history:
        print("Calculation History:")
        for entry in history:
            print(entry)
    else:
        print("Calculation History is empty.")

# Main function to run the calculator app
def main():
    history = []  # Empty list to store calculation history1
    while True:
        print("\033[92m+--------------------------------------+\033[0m")
        print("\033[92m|            CALCULATOR                |\033[0m")

        print("\033[92m+--------------------------------------+\033[0m")
        print("\033[92m|\033[0m"+"\033[93m   Welcome to Simple Calculator App   \033[0m" + "\033[92m|\033[0m")
        # print("\033[92m|\033[0m")
        print("\033[92m+--------------------------------------+\033[0m")
        print("\033[92m|   1. Add                             |\033[0m")
        print("\033[92m|   2. Subtract                        |\033[0m")
        print("\033[92m|   3. Multiply                        |\033[0m")
        print("\033[92m|   4. Divide                          |\033[0m")
        print("\033[92m|   5. Show History                    |\033[0m")
        print("\033[91m|   6. Exit                            |\033[0m")
        print("\033[92m+--------------------------------------+\033[0m")
        print("\033[92m|          MADE BY ANSH Arora          |\033[0m")
        print("\033[92m+--------------------------------------+\033[0m")


        choice = input("\033[94mEnter your choice (1-6)-:  \033[0m")

        if choice == '6':
            print("""\033[33m
            TTTTT  H   H  AAAAA  N   N  K   K     Y   Y  OOOOO  U   U
              T    H   H  A   A  NN  N  K  K       Y Y  O     O U   U
              T    HHHHH  AAAAA  N N N  KK          Y   O     O U   U
              T    H   H  A   A  N  NN  K  K       Y    O     O U   U
              T    H   H  A   A  N   N  K   K     Y      OOOOO   UUU
            \033[0m""")

            print("\033[91m                    For using the calculator. Goodbye!       \033[0m")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("\033[35mEnter first number-: \033[0m"))
            num2 = float(input("\033[35mEnter second number-: \033[0m"))

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            print("Result:", result)
            history.append(operation)

        elif choice == '5':
            display_history(history)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
