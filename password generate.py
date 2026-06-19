import random
import string

# Characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation

# Password length
length = int(input("Enter password length: "))

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)