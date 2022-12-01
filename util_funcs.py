"""this module contain useful functions for creating and encoding and locking a text file
for the encoded message given. """
import random
import string
import sys
import os
import typing

import command_functions
import print_functions


def generate_lock_file(size):
    """this function calls another function to create a unique random name for the text file
    and calls another function to put the code content into that file. """

    lock_file_name = generate_unique_lock_file_name()
    try:
        return write_to_lock_file(lock_file_name, size)
    except Exception as file_error:
        print(f'\n\tAn error occurred while trying to write to {lock_file_name}:{file_error}\n')
        return None


def generate_unique_lock_file_name():
    """this function is the first part of creating a unique random name for a text file.
    It checks if the name already exists and if it does not, then it returns the random file
    name. """
    files_in_dir = os.listdir()
    while True:
        random_file_name = '_lock.txt'
        for _ in range(8):
            random_letter = random.choice(string.ascii_letters)
            random_file_name = random_letter + random_file_name
        if random_file_name not in files_in_dir:
            break
    return random_file_name


def write_lock_values_to_file(num_values: int, file_obj: typing.TextIO):
    """this function uses a loop to go through the encoded message and put it in the text
    file created for the encryption. """

    for line_ct in range(int(num_values)):
        rand_int1 = random.randint(0, sys.maxsize)
        if line_ct < int(num_values) - 1:
            print(f'{rand_int1}', file=file_obj)
            continue
        file_obj.write(f'{rand_int1}')


def write_to_lock_file(file_name, size_val):
    """this function opens the file that was created and calls the write_lock_values_to_file
    function to put the coded content into the file. """
    with open(file_name, 'w') as text_file:
        write_lock_values_to_file(size_val, text_file)
        return file_name


def parse_command_line_args(arg_list: list):
    """this function checks how many arguments were given in the command line when the program
    was called. Based on the number of command line arguments and the command flag
    extracted from ‘arg_list[1]’, the appropriate command function is called"""

    arg_list_len = len(arg_list)
    if arg_list_len == 1:
        print_functions.print_welcome_message()

    elif arg_list_len == 2:
        command = arg_list[1]
        if command == '-help' or command == '-h':
            command_functions.help_command()

        elif command == '-msg':
            # displays list of decrypted plain text message files
            command_functions.msg_command()

        elif command == '-locked':
            # displays list of encrypted (locked) files
            command_functions.locked_command()

        elif command == '-clear':
            # gather all text files from current directory (use list comprehension)
            command_functions.clear_command()
        else:
            print('Error: invalid command')

    elif arg_list_len == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command(arg_list)
        else:
            print('Error: invalid command')

    elif arg_list_len == 4:
        if arg_list[1] == '-lock':
            # check if an int is passed as the lock depth
            command_functions.lock_command(arg_list)
        else:
            print('Error: invalid command')

    else:
        print('Error: invalid command')


def lock_depth_positive_check(depth, arg_val):
    """this function checks if the lock depth argument is a positive number, and returns None
    if it's negative, and returns the int if it's valid. """
    if depth <= 0:
        print(f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n')
        return None
    return depth


def validate_lock_depth(arg_value: str):
    """this function checks if the lock depth given in the command argument is an integer"""

    try:
        lock_depth = int(arg_value)
        return lock_depth_positive_check(lock_depth, arg_value)
    except ValueError:
        print(f'\n\tInvalid lock depth: \'{arg_value}\'. Must be an integer greater than 0 (zero).\n')
    return None
