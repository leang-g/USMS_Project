"""Input validation helpers."""


def get_menu_choice(prompt, minimum, maximum):
    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue

        if minimum <= choice <= maximum:
            return choice

        print(f"Please choose a number from {minimum} to {maximum}.")
