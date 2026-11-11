
import string

print("===================================")
print("      PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

# Check password requirements
length_check = len(password) >= 8

number_check = any(char.isdigit() for char in password)

uppercase_check = any(char.isupper() for char in password)

symbol_check = any(char in string.punctuation for char in password)

# Calculate strength score
score = sum([
    length_check,
    number_check,
    uppercase_check,
    symbol_check
])

# Determine password strength
if score <= 1:
    strength = "WEAK"
elif score <= 3:
    strength = "MEDIUM"
else:
    strength = "STRONG"

# Display results
print("\n========== RESULTS ==========")

print("Password Length:", len(password))
print("Contains 8 Characters:", length_check)
print("Contains Number:", number_check)
print("Contains Uppercase:", uppercase_check)
print("Contains Symbol:", symbol_check)

print("-----------------------------")
print("PASSWORD STRENGTH:", strength)
print("=============================")
