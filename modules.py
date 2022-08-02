import colorama as co

from token_generator_module import generate_token, check_token

from datetime import datetime as dt

from os import path

import os

co.init()
green = co.Fore.GREEN
red = co.Fore.RED
white = co.Fore.WHITE
magenta = co.Fore.MAGENTA
yellow = co.Fore.YELLOW


def menu() -> str:
    option = 'P'
    signal = False
    error_option = False

    while (option != '1' and option != '2' and option != '3' and option != '4'):
        print(magenta + '\t\t<<---------------MENU------------------>>')
        print('\n\t 1: Store token in a file ')
        print('\n\t 2: Generate token without file ')
        print('\n\t 3: View stored tokens ')
        print('\n\t 4: Exit')
        option = input('\n\t---->' + magenta)
        if len(option) > 1:
            signal = True
        if signal:
            signal = False
            print('\n\t The option only can containt 1 character')
            while(len(option) != 1):
                option = input('\t----> ')
        if (option != '1' and option != '2' and option != '3' and option != '4'):
            error_option = True
        if error_option:
            error_option = False
            print(red + '\n\t The choice option is wrong!!\n')

    return option


def encrypt_operation() -> str:
    word = ''
    while(len(word) < 6):
        word = input(
            'Enter a word or phrase (Must contain a minimum of 6 characters) \n\t')

    token = generate_token(word)
    print('\tToken-->' + str(token))

    if (check_token(word, token)):
        print('\tPassword successfully verified')

    data = word + '||' + str(token) + '||created:' + str(dt.now()) + '||'
    return str(data)


def generate_file(data: str) -> None:
    secure_file = '\\data\\secure.bin'
    location = os.getcwd() + secure_file
    print(location)
    if path.exists(location):
        print('\tThe bynary file already exist, adding new data\n')
        mode = 'ab'
    else:
        print('\tThe file was created correctly\n')
        mode = 'wb'
    file = open(secure_file, mode)
    new_data = data + '\n'
    file.write((new_data.encode('utf-8')))
    file.close()
