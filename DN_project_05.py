def introduction():
    print("Welcome to the Number Adder Program!")
    print("This program will prompt you for two whole numbers and add them together.")
    print("You can keep adding numbers or exit the program when you're ready.")

def get_numbers():
    while True:
        try:
            number1 = int(input("Please enter the first whole number: "))
            number2 = int(input("Please enter the second whole number: "))
            return number1, number2
        except ValueError:
            print("Invalid input! Please enter whole numbers.")

def main():
    introduction()
    while True:
        number1, number2 = get_numbers()
        result = number1 + number2
        print(f"The sum of {number1} and {number2} is {result}.")

        exit_program = input("Would you like to add more numbers? (yes/no): ").strip().lower()
        if exit_program == 'no':
            print("Thank you for using the Number Adder Program. Goodbye!")
            break

if __name__ == "__main__":
    main()
