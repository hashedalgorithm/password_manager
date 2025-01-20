import hashlib
import requests

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"


def check_if_password_is_leaked(password: str) -> bool:
    try:
        if (len(password) < 3):
            raise ValueError(f"password should be more 2 or 3 characters long")

        # hash the password using SHA1
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        response = requests.get(f"{HIBP_API_URL}{prefix}")

        if response.status_code == 200:
            if suffix in response.text:
                return True
        return False

    except ValueError as ve:
        print(f"Value Error: {ve}")
        return False
