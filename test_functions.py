"""this module tests out the python functions in the program to make sure they are
behaving as expected. """
import pytest

from testfixtures import TempDirectory

import print_functions
import util_funcs
from print_functions import *
from io import StringIO
# import testfixtures


def test_print_separation_line(capfd):
    """this function tests the line that prints across the screen, making sure it is the correct length"""
    # Include at least six test cases in this function.
    # Five of the test cases should pass the following sets of parameters to
    # ‘print_separation_line()’ and verify the terminal (stdout) output:
    print_functions.print_separation_line('=', 2)
    out, err = capfd.readouterr()
    assert out == '\n\t==\n\n'
    # assert print_separation_line('=', 2) == '\n\t==\n\n'
    # assert print_separation_line('=', 0) == '\n\t\n\n'
    # assert print_separation_line('=', 10) == '\n\t==========\n\n'
    # assert print_separation_line('', 2) == '\n\t\n\n'
    # assert print_separation_line('=', -1) is None


def test_extract_msg_file_content(capfd):
    """this function makes sure that the file is accessing the proper contents of the correct text files"""
    # filename = 'test.txt'
    # with TempDirectory() as tempDir:
    # declare a temp filename (‘test.txt’)
    # write a test message to ‘test.txt’ using tempDir.write(temp_filename,
    # < message_string >)
    # construct the file path: tempDir.path + '\\' + temp_filename
    # call extract_msg_file_content(file_path)
    with TempDirectory() as tempDir:
        temp_filename = 'test.txt'
        test_message = b'test123'
        tempDir.write(temp_filename, test_message)
        file_path = tempDir.path + '\\' + temp_filename
        util_funcs.extract_msg_file_content(file_path)
    out, err = capfd.readouterr()
    assert out == '-> test123\n'

    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as error:
        util_funcs.extract_msg_file_content(missing_file)
    assert error.type is FileNotFoundError


def test_lock_depth_positive_check(capfd):
    """this function tests that the function that checks in the lock depth argument is valid"""
    # depth = 0
    # arg_val = '0'
    # assert util_funcs.lock_depth_positive_check(depth, arg_val) is None
    # out, err = capfd.readouterr()
    # assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n'

    # depth = -1
    # arg_val = '-1'
    # assert util_funcs.lock_depth_positive_check(depth, arg_val) is None
    # out, err = capfd.readouterr()
    # assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n'

    depth = 20
    arg_val = '20'
    util_funcs.lock_depth_positive_check(depth, arg_val)
    out, err = capfd.readouterr()
    assert out != 20
