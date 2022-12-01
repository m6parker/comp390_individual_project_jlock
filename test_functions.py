"""this module tests out the python functions in the program to make sure they are
behaving as expected. """
import pytest
from testfixtures import TempDirectory

import util_funcs
from print_functions import *
from util_funcs import lock_depth_positive_check


def test_print_separation_line(capfd):
    """this function tests the line that prints across the screen, making sure it is the correct length"""
    # Include at least six test cases in this function.
    # Five of the test cases should pass the following sets of parameters to
    # ‘print_separation_line()’ and verify the terminal (stdout) output:
    assert print_separation_line('=', 2) == '\n\t==\n\n'
    assert print_separation_line('=', 0) == '\n\t\n\n'
    assert print_separation_line('=', 10) == '\n\t==========\n\n'
    assert print_separation_line('', 2) == '\n\t\n\n'
    assert print_separation_line('=', -1) is None


def test_extract_msg_file_content(capfd):
    """this function makes sure that the file is accessing the proper contents of the correct text files"""
    # filename = 'test.txt'
    # with TempDirectory() as tempDir:
    # declare a temp filename (‘test.txt’)
    # write a test message to ‘test.txt’ using tempDir.write(temp_filename,
    # < message_string >)
    # construct the file path: tempDir.path + '\\' + temp_filename
    # call extract_msg_file_content(file_path)


def test_lock_depth_positive_check(capfd):
    """this function tests that the function that checks in the lock depth argument is valid"""
    assert util_funcs.lock_depth_positive_check(20, '20') == 20
    assert util_funcs.lock_depth_positive_check(0, '0') is None