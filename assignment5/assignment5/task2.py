def check_pin_format(pin):
    if pin.isdigit():
        return True
    return False


def check_pin_length(pin):
    if len(pin) == 4 or len(pin) == 6:
        return True
    return False


def check_pin_consecutive_repeat_rule(pin):
    for i in range(len(pin)-1):
        if pin[i] == pin[i + 1]:
            return False
    return True


def is_pin_code_validate(pin):
    if check_pin_format(pin) and check_pin_length(pin) and check_pin_consecutive_repeat_rule(pin):
        return True
    return False


pin_code1 = input('Please enter pin-code: ')
if is_pin_code_validate(pin_code1):
    pin_code2 = input('Please confirm your pin-code: ')
    if pin_code1 == pin_code2:
        print('Your validation is successful')
    else:
        print('Two passwords are not matched')
else:
    print('Pin-code is incorrect')
