'''
    ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
    If the function is passed a valid PIN string, return true, else return false.
    Examples:
    "1234"   -->  true
    "12345"  -->  false
    "a234"   -->  false
'''


def validate_pin(pin):
    return True if (len(pin) == 6 and pin.isdigit()) or (len(pin) == 4 and pin.isdigit()) else False

print(validate_pin('10-27'))

# good solution
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()