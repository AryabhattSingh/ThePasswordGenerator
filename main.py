from characters_treasury import *
import random

print("""
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
""", end="")

print("""
                    Welcome to The PyPassword Generator!
                One-stop shop for all your password needs!
""")

upper_case_count = input("How many Upper Case LETTERS would you like in your password? : ")

if not upper_case_count.isnumeric():
    print("\nKindly enter a valid number")
else:
    lower_case_count = input("How many Lower Case LETTERS would you like in your password? : ")
    if not lower_case_count.isnumeric():
        print("\nKindly enter a valid number")
    else:
        symbols_count = input("How many SYMBOLS would you like in your password? : ")
        if not symbols_count.isnumeric():
            print("\nKindly enter a valid number")
        else:
            num_count = input("How many NUMBERS would you like in your password? : ")
            if not num_count.isnumeric():
                print("\nKindly enter a valid number")
            else:
                upper_case_count = int(upper_case_count)
                lower_case_count = int(lower_case_count)
                symbols_count = int(symbols_count)
                num_count = int(num_count)

                password_list = []

                for i in range(0, upper_case_count):
                    random_index = random.randint(0, len(upper_case_alphabets) - 1)
                    password_list.append(upper_case_alphabets[random_index])

                for i in range(0, lower_case_count):
                    random_index = random.randint(0, len(lower_case_alphabets) - 1)
                    password_list.append(lower_case_alphabets[random_index])

                for i in range(0, symbols_count):
                    random_index = random.randint(0, len(symbols) - 1)
                    password_list.append(symbols[random_index])

                for i in range(0, num_count):
                    random_index = random.randint(0, len(numbers) - 1)
                    password_list.append(numbers[random_index])

                # Randomize / Shuffle the password list
                # random.shuffle() function randomizes the elements of a mutable sequence. Not applied on strings
                random.shuffle(password_list)

                password_string = ""
                for elements in password_list:
                    password_string += elements

                print(f"\n{('*' * 45)}\n"
                      f"Generated Password is {password_string}"
                      f"\n{('*' * 45)}\n"
                      f"\nDidn't like it? Run the program again.")
