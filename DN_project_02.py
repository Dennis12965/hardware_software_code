def introduction():
    print("Welcome to my conversation program!")
    print("I will keep asking questions until you type 'exit'.")

def ask_question():
    name = input("What is your name? ")
    favorite_show = input(f"What is your favorite show, {name}? ")
    favorite_sport = input("What is your favorite sport, " + name + "? ")
    input(f"Cool! {favorite_sport} is awesome!")
    input("Do you like programming? (yes/no) ")
    input(" Thanks for chatting with me")
def conversation():
    count = 0
    while True:
        favorite_show = ask_question()
        if favorite_show.strip().lower() == 'exit':
            break
        count += 1
    return count

def closing_statement(count):
    print(f"Thanks for chatting with me! You answered {count} questions.")

def main():
    introduction()
    count = conversation()
    closing_statement(count)


main()
