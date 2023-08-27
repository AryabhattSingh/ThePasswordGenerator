# The Password Generator

Welcome to the Password Generator project! This program allows you to create strong and secure passwords tailored to your preferences. It features a user-friendly interface,
password requirement customization, and secure randomization techniques.

## Introduction

In today's digital age, maintaining the security of your online accounts is of utmost importance. A crucial aspect of account security is using strong and unique passwords.
The Password Generator simplifies this task by enabling you to generate passwords that meet your specific criteria.

## Features

- **ASCII Art Welcome:** The program greets you with an eye-catching ASCII art and a friendly message, setting the tone for a positive user experience.

- **Customizable Passwords:** You have the freedom to define your password requirements, including:
  - The number of upper-case letters you desire.
  - The number of lower-case letters you'd like.
  - The count of symbols or special characters in the password.
  - The count of numerical digits in the password.

- **Input Validation:** The program ensures the validity of your inputs using the `str.isnumeric()` function. This function prevents negative, fractional numbers, and any
  other inappropriate inputs, ensuring a smooth and error-free experience.

- **Characters Treasury:** The project includes a module called `characters_treasury.py` that houses all possible characters that can be used for password generation. This
  centralized collection of characters ensures consistent and secure password generation.

- **Initial Generation:** Once the user's input is validated, the program initializes an empty list. This list will hold the random characters selected based on the user's
   inputs. It populates the list with the specified number of random upper-case and lower-case letters, symbols, and digits.

- **Randomization Technique:** To prevent the clustering of characters from the same category, the program utilizes the `random.shuffle(sequence)` function. This function
  shuffles the sequence in place, promoting randomness and enhancing password security. The `sequence` must be mutable for the shuffling function to work.

- **Password Generation:** The program combines the characters in the shuffled list to create a final password string.

- **User-Friendly Display:** Finally, the generated password is displayed to you, ensuring that you have immediate access to your new secure password.

## Getting Started

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the `main.py` script using a Python interpreter.
4. Follow the on-screen prompts to specify your password requirements.
5. Receive your generated password and use it to enhance your account security!

## Dependencies

This project is written in Python. No external libraries are required, as it solely relies on Python's built-in functions and modules.

## Contributions

Contributions to this project are welcome! If you find any bugs, have suggestions for improvements, or want to add more features, feel free to fork this repository and 
submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project for personal and commercial purposes.

---

Thank you for checking out the Password Generator project. We hope this tool helps you create strong and secure passwords effortlessly. Your online security matters!
