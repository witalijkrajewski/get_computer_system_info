from .run_process import run_operation


def validate_input(value):
    if value.isdigit():
        user_choice = int(value)
        return True
    return False


def convert_input_str_in_int(value):
    if validate_input(value):
        return int(value)


def start_app():
    while True:
        print('\nChoose type of operation to run, please:')
        print('1)CPU Information')
        print('2)Memory Information')
        print('3)System Information')
        print('4)Disks Information')
        print('5)Network Information')

        user_choice = input('Enter Operation number or \'0\' to close application:')

        if validate_input(user_choice):
            choice = convert_input_str_in_int(user_choice)
            if choice in [1, 2, 3, 4, 5]:
                run_operation(choice)
            if choice == 0:
                break
