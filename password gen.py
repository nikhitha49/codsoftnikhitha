def generate_password(length):
    # Define character set: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Create a password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Ask user for password length
        length = int(input("Enter desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
