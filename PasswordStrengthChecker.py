import re
import getpass

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[_@$]", password):
        score += 1
    return score

def main():
    password = getpass.getpass("Enter your password: ")
    score = check_password_strength(password)
    if score == 1:
        print("Your password is weak.")
        print("We recommend using a password that is at least 8 characters long and contains upper and lower case letters, numbers, and special characters.")
    elif score == 2:
        print("Your password is moderate.")
        print("We recommend using a password that is at least 8 characters long and contains upper and lower case letters, numbers, and special characters.")
    elif score >= 3:
        print("Your password is strong.")
    else:
        print("Invalid password.")

if __name__ == '__main__':
    main()
