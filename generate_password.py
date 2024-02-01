import secrets
import string


def generate_password(length):
    """
    Generates a random password of the specified length.

    Args:
        length (int): The length of the password.

    Returns:
        str: The randomly generated password.

    Examples:
         generate_password(8)
        'xY3@p9$z'
         generate_password(12)
        'A7!bR2@q5#eZ'
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


if __name__ == '__main__':
    passwd = generate_password(12)
    print(passwd)
