import random

# Function to generate a password
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    
# Generate the password by selecting random characters
    for _ in range(length):
        password += random.choice(characters)
    
    return password

# Store the previously generated password
previous_password = ""

while True:
    password_length = int(input("Enter the length of the password (or 0 to quit): "))
    
    if password_length == 0:
        print("Exiting program...")
        break
    
    # Generate a new password
    new_password = generate_password(password_length)
    
    # Check if the new password is the same as the previous one
    while new_password == previous_password:
        print("Generated password is the same as the last one. Generating a new password...")
        new_password = generate_password(password_length)
    
    # Display the password
    print(f"Generated password: {new_password}")
    
    # Update previous_password to the current one
    previous_password = new_password