from CPU.cpu_information import get_cpu_information
from Memory.memory_information import get_memory_information
from System.system_information import get_system_information
from Disks.disks_information import get_disks_information
from Network.network_information import get_network_information


def run_operation(value):
    if value == 1:
        return get_cpu_information()
    elif value == 2:
        return get_memory_information()
    elif value == 3:
        return get_system_information()
    elif value == 4:
        return get_disks_information()
    elif value == 5:
        return get_network_information()
    