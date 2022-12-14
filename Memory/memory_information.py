from Size.size import get_size

import psutil
import platform


def get_memory_information():
    print('=' * 40, ' Virtual Memory Info', '=' * 40)

    svmem = psutil.virtual_memory()
    print(f'Volume: {get_size(svmem.total)}')
    print(f'Available: {get_size(svmem.available)}')
    print(f'In usage: {get_size(svmem.used)}')
    print(f'Percent: {svmem.percent}%')

    print('=' * 40, 'Swap Memory Info', '=' * 40)
    swap = psutil.swap_memory()
    print(f'Volume: {get_size(swap.total)}')
    print(f'Available: {get_size(swap.free)}')
    print(f'In usage: {get_size(swap.used)}')
    print(f'Percent: {swap.percent}%')
