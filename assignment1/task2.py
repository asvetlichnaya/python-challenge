# Assignment1, Task2
def contains_digits(value: str):
    for i in value:
        if i.isdigit():
            print("User name can’t include any numeric characters (digits)")
            return True
    return False


def contains_more_than_n_symbols(value: str, n: int):
    if len(value) > n:
        print('User name can not exceed ', n, ' characters')
        return True
    return False


def starts_with_prefix(value: str, prefix: str):
    if value.lower().startswith(prefix.lower()):
        return True
    else:
        print('Email address must start with user name')
        return False


def is_in_lowercase(value: str):
    if value.islower():
        return True
    else:
        print('All email letters must be in lower case')
        return False


def ends_with_suffix(value: str, suffix: str):
    if value.lower().endswith(suffix.lower()):
        return True
    else:
        print('Email address must end with ', suffix)
        return False


def contains_whitespace(value: str):
    if ' ' in value:
        print('Please validate that there are no whitespaces in email address')
        return True
    return False


def contains_underscore(value: str):
    if '_' in value:
        return True
    print('Email address must include underscore (_) character')
    return False


user_name = input('Please input your name: ').strip()
while contains_digits(user_name) or contains_more_than_n_symbols(user_name, 15):
    user_name = input('Please input your name: ').strip()

user_email = input('Please input an email address: ').strip()
while not starts_with_prefix(user_email, user_name) or not is_in_lowercase(user_email) or \
         not ends_with_suffix(user_email, '@gmail.com') or not contains_underscore(user_email) or \
         contains_whitespace(user_email):
    user_email = input('Please input an email address: ').strip()
