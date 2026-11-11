
print("======================================")
print("       ENCRYPTION & DECRYPTION")
print("           CAESAR CIPHER")
print("======================================")

# Get input from user
text = input("Enter the text: ")

# Get shift key
shift = int(input("Enter the shift key: "))

# Encryption function
def encrypt(message, key):
    result = ""

    for char in message:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))

        else:
            result += char

    return result


# Decryption function
def decrypt(message, key):
    return encrypt(message, -key)


# Perform encryption
encrypted_text = encrypt(text, shift)

# Perform decryption
decrypted_text = decrypt(encrypted_text, shift)

# Display results
print("\n========== RESULTS ==========")
print("Original Text  :", text)
print("Encrypted Text :", encrypted_text)
print("Decrypted Text :", decrypted_text)
print("=============================")
