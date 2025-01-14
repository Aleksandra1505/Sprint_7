import random
import string


def generate_login_password_name():
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    login = generate_random_string(11)
    password = generate_random_string(11)
    first_name = generate_random_string(11)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }