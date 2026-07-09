"""Input validation helpers."""

def get_valid_input(prompt, valid_options):
    """Get input and validate it's in the list of valid options"""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print(f"❌ Invalid input. Please choose: {', '.join(valid_options)}")

def get_float(prompt):
    """Get a valid float number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number (e.g., 3.5)")

def get_int(prompt):
    """Get a valid integer from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number")
