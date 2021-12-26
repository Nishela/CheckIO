'''In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string.

Output: A bool.'''


# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    all_digits = all(map(lambda x: x.isdigit(), password.replace(' ', '')))
    all_alpha = all(map(lambda x: x.isalpha(), password.replace(' ', '')))
    if len(password) > 6 and not all_digits and not all_alpha:
        return True
    else:
        return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

