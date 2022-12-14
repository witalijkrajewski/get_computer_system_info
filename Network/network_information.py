from Size.size import get_size

import psutil


def get_network_information():
    print('='*40, 'Network Information', '='*40)
    if_addrs = psutil.net_if_addrs()

    for interface_name, interface_address in if_addrs.items():
        for address in interface_address:
            print(f'=== Interface: {interface_name} ===')
            if str(address.family.name) == 'AF_INET':
                print(f'IP: {address.address}')
                print(f'Network Mask: {address.netmask}')
                print(f'Broadcast IP-address: {address.broadcast}')
            elif str(address.family) == 'AF_PACKET':
                print(f'MAC-address: {address.address}')
                print(f'Network Mask: {address.netmask}')
                print(f'Broadcast MAC: {address.broadcast}')

    net_io = psutil.net_io_counters()
    print(f'Total Bytes Sent: {get_size(net_io.bytes_sent)}')
    print(f'Total Bytes Received: {get_size(net_io.bytes_recv)}')

