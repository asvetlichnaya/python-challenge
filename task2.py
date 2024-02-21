import string


def contains_digits(value: str):
    if not value.isalpha():
        print("User name can’t include any numeric characters (digits)")
        return True
    return False


def contains_more_than_n_symbols(value: str, n: int):
    if len(value) > 15:
        print('User name can not exceed ', n, ' characters')
        return True
    return False


def starts_with_prefix(value: str, prefix: str):
    if value.strip().lower().startswith(prefix.lower()):
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
    if value.strip().lower().endswith(suffix.lower()):
        return True
    else:
        print('Email address must end with @ubs.com')
        return False


def contains_whitespace(value: str):
    for i in value:
        if i in string.whitespace:
            print('Please validate that there are no whitespaces in email address')
            return True
    return False


def contains_underscore(value: str):
    for i in value:
        if i in '_':
            return True
    print('Email address must include underscore (_) character')
    return False


user_name = input('Please input your name: ')
while contains_digits(user_name) or contains_more_than_n_symbols(user_name, 15):
    user_name = input('Please input your name: ')

user_email = input('Please input an email address: ')
while not starts_with_prefix(user_email, user_name) or not is_in_lowercase(user_email) or \
         not ends_with_suffix(user_email, '@ubs.com') or not contains_underscore(user_email) or \
         contains_whitespace(user_email):
    user_email = input('Please input an email address: ')
