
import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all_characters = lowercase + uppercase + numbers + symbols

secure_random = random.SystemRandom()

print("=" * 40)
print("       PASSWORD GENERATOR")
print("=" * 40)

while True:

    try:
        length = int(input("\nEnter password length (minimum 4): "))
        count = int(input("How many passwords do you want? "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        if count <= 0:
            print("Please enter a positive number.")
            continue

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    print("\nGenerated Passwords:")
    print("-" * 40)

    for i in range(count):

        password = [
            secure_random.choice(lowercase),
            secure_random.choice(uppercase),
            secure_random.choice(numbers),
            secure_random.choice(symbols)
        ]

        for j in range(length - 4):
            password.append(secure_random.choice(all_characters))

        secure_random.shuffle(password)

        password = "".join(password)

        print("Password", i + 1, ":", password)

    print("-" * 40)

    choice = input("\nGenerate more passwords? (yes/no): ").strip().lower()

    if choice not in ("yes", "y"):
        print("\nThank you for using Password Generator!")
        break
