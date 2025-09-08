"""
Simple Password Strength Checker

Ask user for a password
Check if it meets criteria: at least 8 characters, has uppercase, lowercase, and numbers
Use loops to count each type of character
Keep asking until they provide a strong password
"""

def check_password_strength(password):
    # Initialize counters
    has_upper = False
    has_lower = False
    has_digit = False
    length = len(password)
    
    # Loop through each character to check types
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    # Check all criteria
    if length >= 8 and has_upper and has_lower and has_digit:
        return True, "Password is strong!"
    else:
        reasons = []
        if length < 8:
            reasons.append("at least 8 characters")
        if not has_upper:
            reasons.append("an uppercase letter")
        if not has_lower:
            reasons.append("a lowercase letter")
        if not has_digit:
            reasons.append("a number")
        return False, f"Password is weak. It needs: {', '.join(reasons)}"

# Main loop to keep asking until strong password
while True:
    password = input("Enter a password: ")
    is_strong, message = check_password_strength(password)
    print(message)
    if is_strong:
        break
