from string import ascii_lowercase


def is_valid_username(username: str) -> bool:
    username = username.lower()
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^`{|}~"""
    for character in username:
        if character in punctuation:
            print(character)
            return False

    if username == "":
        return False
    elif len(username) < 6:
        return False
    elif len(username) > 12:
        return False

    if username[0] not in ascii_lowercase:
        return False
    else:
        return True

    # for i in username[0]:
    #     if i not in ascii_lowercase:
    #         return f"{i} no pasa"
    #     else:
    #         return username
