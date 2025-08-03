import re

def check_password_strength(password):
    # Criteria definitions
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # List of error messages
    errors = []
    if length_error:
         errors.append(" Password should be at least 8 characters.")
    if lowercase_error:
        errors.append(" Add at least one lowercase letter.")
    if uppercase_error:
        errors.append(" Add at least one uppercase letter.")
    if digit_error:
        errors.append(" Include at least one number.")
    if special_char_error:
        errors.append(" Use at least one special character (!@#$...).")

    # Strength calculation
    passed_criteria = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])
    if passed_criteria == 5:
        strength = " Strong Password"
    elif 3 <= passed_criteria < 5:
        strength = " Moderate Password"
    else:
        strength = " Weak Password"

    return strength, errors

# Main function
def main():
    print("Password Complexity Checker ")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength: ", strength)
    print("\nFeedback:")
    for msg in feedback:
        print(msg)

# Run the program
if __name__ == "__main__":
    main()
