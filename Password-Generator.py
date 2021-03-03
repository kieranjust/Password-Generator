import random
import string


def password_generator():
    while True:
        try:
            characters = int(input("How many characters would you like in your password? (Max 50)"))

        except ValueError:
            print("Please use numeric keys to enter a number between 1-50.")
            continue

        while characters < 0 or characters > 50:
            characters = int(input("Please enter a number between 1 and 50."))

        password_characters = random.sample(string.ascii_letters, k=characters)
        password = ''.join(password_characters)
        print(password)
        break


password_generator()
