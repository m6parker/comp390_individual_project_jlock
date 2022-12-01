"""this is the main module where the arguments taken from the command line are
put into a list and appropriate functions are called accordingly"""
import sys
import util_funcs


def jlock_main():
    """this function takes the command line arguments into a list and calls the command line args
    function from the util_funcs module. It also makes sure there's no quotes so it won't crash"""
    # get command line arguments
    arg_list = sys.argv
    if '' in arg_list:
        print('Error: invalid command')
        return
    util_funcs.parse_command_line_args(arg_list)


if __name__ == '__main__':
    """this function calls the jlock_main function to start the program. """
    jlock_main()
