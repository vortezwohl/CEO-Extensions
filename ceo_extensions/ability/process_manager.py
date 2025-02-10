import psutil
from ceo import ability


@ability
def show_specifications_of_current_computer(**kwargs) -> str:
    """
        Returns a string representation of the current computer's hardware specifications.

        You may need unit conversions before you generate the answers, don't forget to calculate them with "constant_calculate"
        For example: the unit Mhz should be converted to GHz, the unit Bytes may be converted to Gigabytes(GB)...

        This function collects various hardware information, including CPU details, memory, swap_memory, disk partitions, disk usage,
        network I/O, and network interfaces.

        Args:
            **kwargs: Arbitrary keyword arguments (not used in this function).

        Returns:
            str: A JSON-style string containing the computer's hardware specifications.
    """
    return str({
        'cpu_logical_cores': psutil.cpu_count(logical=True),
        'cpu_physical_cores': psutil.cpu_count(logical=False),
        'cpu_frequency(Mhz)': psutil.cpu_freq(),
        'memory(Byte)': psutil.virtual_memory(),
        'swap_memory(Byte)': psutil.swap_memory(),
        'disk_partitions': psutil.disk_partitions(),
        'disk_usage(Byte)': psutil.disk_usage('/'),
        'net_io(Byte)': psutil.net_io_counters(),
        'net_interfaces': psutil.net_if_addrs()
    })
