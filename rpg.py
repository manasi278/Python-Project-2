import random
import string

def generate_password(length, chars):
    """Generate a password with the specified length and character set."""
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Simple Password Generator")
    length = int(input("Enter password length: "))

    
    chars = ""
    if input("Include letters? (y/n): ").strip().lower() == 'y':
        chars += string.ascii_letters
    if input("Include numbers? (y/n): ").strip().lower() == 'y':
        chars += string.digits
    if input("Include symbols? (y/n): ").strip().lower() == 'y':
        chars += string.punctuation

    
    if not chars:
        print("Error: No character types selected. Please try again.")
        return

    
    password = generate_password(length, chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
