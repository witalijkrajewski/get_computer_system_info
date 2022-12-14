from Size.size import get_size

import psutil
import platform


def get_disks_information():
    print('=' * 40, 'Disks Information', '=' * 40)

    partitions = psutil.disk_partitions()

    for partition in partitions:
        print(f'=== Disk: {partition.device} ===')
        print(f'Type of file system: {partition.fstype}')
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

        print(f'Total Volume: {get_size(partition_usage.total)}')
        print(f'In Usage: {get_size(partition_usage.used)}')
        print(f'Available: {get_size(partition_usage.free)}')
        print(f'Percent: {partition_usage.percent}%')
