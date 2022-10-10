import random

def create_password():
    upper_case1 = chr(random.randint(65, 90))
    upper_case2 = chr(random.randint(65, 90))
    upper_case3 = chr(random.randint(65, 90))
    lower_case1 = chr(random.randint(97, 122))
    lower_case2 = chr(random.randint(97, 122))
    lower_case3 = chr(random.randint(97, 122))
    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))
    digit3 = chr(random.randint(48, 57))
    digit4 = chr(random.randint(48, 57))
    spec_char1 = chr(random.randint(33, 38))
    spec_char2 = chr(random.randint(33, 38))
    return upper_case1, upper_case2, upper_case3, lower_case1, lower_case2, lower_case3, digit4, digit3, digit2, digit1, spec_char2, spec_char1