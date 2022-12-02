"""this module tests out the python functions in the program to make sure they are
behaving as expected. """
import pytest
from testfixtures import TempDirectory

import print_functions
import util_funcs
from print_functions import *


def test_print_separation_line(capfd):
    """this function tests the line that prints across the screen that keeps everything organized.
    It tests it using different lengths (2, 0, 10, -1) and once without the line character """
    # Include at least six test cases in this function.
    # Five of the test cases should pass the following sets of parameters to
    # ‘print_separation_line()’ and verify the terminal (stdout) output:
    print_functions.print_separation_line('=', 2)
    out, err = capfd.readouterr()
    assert out == '\n\t==\n\n'

    print_functions.print_separation_line('=', 0)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'

    print_functions.print_separation_line('=', 10)
    out, err = capfd.readouterr()
    assert out == '\n\t==========\n\n'

    print_functions.print_separation_line('', 2)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'

    print_functions.print_separation_line('=', -1)
    out, err = capfd.readouterr()
    assert out == '\n\t\n\n'


def test_extract_msg_file_content(capfd):
    """this function makes sure that the file is accessing the proper contents of the correct text files.
    a test file is created with a test message and the file path is created from that. then the function
    extract_msg_file_contents is called using the test file name and the output is shown."""

    with TempDirectory() as tempDir:
        temp_filename = 'test.txt'
        test_message = b'test123'
        tempDir.write(temp_filename, test_message)
        file_path = tempDir.path + '\\' + temp_filename
        extract_msg_file_content(file_path)
    out, err = capfd.readouterr()
    assert out == ' -> test123\n'

    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as error:
        extract_msg_file_content(missing_file)
    assert error.type is FileNotFoundError


def test_lock_depth_positive_check(capfd):
    """this function tests that the lock_depth_positive_check() function is valid by using an integer, a negative
    number, and zero. the error message is shown for those that were not an int greater than zero."""
    depth = 0
    arg_val = '0'
    assert util_funcs.lock_depth_positive_check(depth, arg_val) is None
    out, err = capfd.readouterr()
    assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n\n'

    depth = -10
    arg_val = '-10'
    assert util_funcs.lock_depth_positive_check(depth, arg_val) is None
    out, err = capfd.readouterr()
    assert out == f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n\n'

    depth = 20
    arg_val = '20'
    util_funcs.lock_depth_positive_check(depth, arg_val)
    out, err = capfd.readouterr()
    assert out != 20
