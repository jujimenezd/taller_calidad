from string import ascii_letters, digits, punctuation


def check_contiditions(password: str):
    password_with_digit = False
    password_with_letters = False
    password_with_symbols = False

    password_with_digits_and_letters = False

    for character in password:
        if character in digits:
            password_with_digit = True

        if character in ascii_letters:
            password_with_letters = True

        if character in punctuation:
            password_with_symbols = True

    if password_with_digit and password_with_letters:
        password_with_digits_and_letters = True

    if password_with_digits_and_letters and password_with_symbols:
        return True
    else:
        return False


def check_password(password: str):
    for character in password:
        if character == " ":
            return False

    if len(password) < 8:
        return False

    check_contidition = check_contiditions(password)
    if check_contidition:
        return True
    else:
        return False


result = check_password("Software$_EnginneR")
print(result)
