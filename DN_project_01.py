def main():

    print("Welcome to the personal information program!")
    print("This program will ask you for some details about yourself, including your name, college, and high school.")
    print()

    name = input("What is your name? ")

    college_name = input("What college do you attend? ")

    high_school_name = input("What high school did you attend? ")

    print("We want to know if you like programming!")
    print()
    print(f"Do you like programming, {name}?")
    answer = input()
    print(f"Great! You said {answer}.")

    print("\nThank you for sharing the information, {}!".format(name))
    print(f"You attend {college_name} and you went to {high_school_name} for high school.")
    print("Let's start learning some Python today!")

if __name__ == "__main__":
    main()
