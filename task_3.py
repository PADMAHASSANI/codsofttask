import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character types
    all_chars = letters + digits + special_chars

    # Generate the password
    password = random.choices(all_chars, k=length)

    # Join the list to form the final password string
    return ''.join(password)

def main():
    while True:
        try:
            # Get user-defined password length
            length = int(input("Enter the desired password length: "))
            
            # Generate and print the password
            print("Generated password:", generate_password(length))
            
            # Ask if the user wants to generate another password or exit
            choice = input("Do you want to generate another password? (y/n): ").strip().lower()
            
            if choice == 'n':
                print("Exiting...")
                break  # Exit the loop and end the program
        except ValueError:
            print("Invalid input, please enter a valid number for the length.")

# Run the program
main()
