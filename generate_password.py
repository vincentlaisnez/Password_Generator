import secrets
import string


def generate_password(length, digits=True, special_char=True):
    """
    Generates a random password of the specified length.

    Args:
        length (int): The length of the password.
        digits (bool, optional): Whether to include digits in the password. Defaults to True.
        special_char (bool, optional): Whether to include special characters in the password. Defaults to True.

    Returns:
        str: The randomly generated password.
"""

    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if special_char:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


if __name__ == '__main__':
    passwd = generate_password(12)
    print(passwd)
