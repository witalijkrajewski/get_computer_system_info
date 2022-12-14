import platform


def get_system_information():
    print('='*40, 'System Information', '='*40)
    uname = platform.uname()

    print(f'System: {uname.system}')
    print(f'Node name: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Machine: {uname.system}')
    print(f'CPU: {uname.processor}')

