def introduction():
    print("Welcome to the Decimal-Binary Converter Program!")
    print("You can convert between decimal and binary numbers.\n")

def convert_decimal_to_binary():
    while True:
        try:
            decimal = int(input("Enter a decimal number: "))
            return bin(decimal)[2:] if decimal >= 0 else print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")

def convert_binary_to_decimal():
    while True:
        binary = input("Enter a binary number: ")
        if all(char in "01" for char in binary):
            return int(binary, 2)
        print("Invalid input! Please enter a valid binary number.")

def main():
    introduction()
    while True:
        choice = input("1. Decimal to Binary\n2. Binary to Decimal\n3. Exit\nChoose an option: ").strip()
        if choice == "1":
            print(f"Binary: {convert_decimal_to_binary()}\n")
        elif choice == "2":
            print(f"Decimal: {convert_binary_to_decimal()}\n")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
