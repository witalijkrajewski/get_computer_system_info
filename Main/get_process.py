from .run_process import run_operation


def start_app():
    while True:
        print('\nChoose type of operation to run, please:')
        print('1)CPU Information')
        print('2)Memory Information')
        print('3)System Information')
        print('4)Disks Information')
        print('5)Network Information')

        user_choice = input('Enter Operation number or \'0\' to close application:')

        if int(user_choice) in [1, 2, 3, 4, 5]:
            run_operation(int(user_choice))

        if int(user_choice) == 0:
            break
