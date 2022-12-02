"""this module contains all the command functions organized. each command prints it's
own functions, they are called by the command line arguments that are taken in the terminal
when the program is run. """
import json
import os

import print_functions
import util_funcs
from lock_functions import lock
from unlock_functions import unlock


def help_command():
    """ Call all the command help print functions. Separate the print calls with a call to
    print_separation_line() so they are divided nicely by a line. """
    print_functions.print_separation_line('=', 50)
    print_functions.print_help_welcome()
    print_functions.print_separation_line('=', 50)
    print_functions.print_lock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_unlock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_msg_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_locked_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_clear_help()
    print_functions.print_separation_line('=', 50)


def msg_command():
    """this function prints out what messages have been 'locked' and then 'unlocked' using the
    encrypter. the name of the encoded text file is shown with an arrow pointing to the
    decrypted message. """
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
    if len(decrypted_file_list) == 0:
        print('\n\tNo plaintext message files available.\n')
    else:
        print('\n\tPlaintext message files:\n')
        for file_name in decrypted_file_list:
            print_functions.print_msg_file_info(file_name)


def locked_command():
    """this function prints out what encrypted text files there currently are that are not
    unlocked yet. It will tell you the txt file name and the encrypted code, but will not reveal the
    message. """

    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    if len(encrypted_file_list) == 0:
        print('\n\tNo encrypted message files available.\n')
    else:
        print('\n\tEncrypted message files:\n')
        for file_name in encrypted_file_list:
            print(f'\t{file_name}')
            with open(file_name, 'r') as encrypt_msg_fileIO:
                json_obj = json.loads(encrypt_msg_fileIO.read())
                print(f'\t\t{json_obj["encrypted_message"]}\n')


def clear_command():
    """this function removes all encrypted and decrypted files from the program,
    erasing everything and starting over, displaying a message when it is done. """

    lock_file_list = [file for file in os.listdir() if file.endswith('_lock.txt')]
    key_file_list = [file for file in os.listdir() if file.endswith('_key.txt')]
    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]

    # assemble ALL text file list
    master_text_file_list = lock_file_list + key_file_list + encrypted_file_list + decrypted_file_list
    # print(master_text_file_list)
    for text_file in master_text_file_list:
        os.remove(text_file)

    print('\n\n\tAll \'lock\', \'key\', \'encrypted message\', and \'decrypted message\' text files removed.\n')


def unlock_command(arg_list: list):
    """this function will take the encrypted txt file name argument and return it to it's
    original message. It unlocked the code, needs to be given the txt file name to decode. """
    target_encrypted_file: str = arg_list[2]
    file_list = os.listdir()
    if (target_encrypted_file in file_list) and (len(target_encrypted_file) == 22) and \
            (target_encrypted_file[-18:] == '_encrypted_msg.txt'):
        unlock(target_encrypted_file)
    else:
        print(f'\n\t{target_encrypted_file} does not exist or is invalid\n')


def lock_command(arg_list: list):
    """this function takes in an integer and a message and creates a text file with the encrypted
    message in it. """
    depth = util_funcs.validate_lock_depth(arg_list[2])
    if depth:
        lock_file = util_funcs.generate_lock_file(arg_list[2])
        lock(arg_list[3], lock_file)
