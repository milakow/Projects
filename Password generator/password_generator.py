import random

import ten_char_password, twelve_char_password

def get_length_of_password():
    password_length = int(input('Select the password length from 10/ 12 characters: '))
    if password_length != 10 and password_length != 12:
        raise ValueError('Wrong number of characters.')
    return password_length

def main():
    password_length = get_length_of_password()
    if password_length == 10:
        list_of_password = list(ten_char_password.create_password())
        for sign in list_of_password:
            random.shuffle(list_of_password)
            print(sign, end='')
    else:
        list_of_password = list(twelve_char_password.create_password())
        for sign in list_of_password:
            random.shuffle(list_of_password)
            print(sign, end='')


if __name__ == '__main__':
    main()
