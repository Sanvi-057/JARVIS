import platform
import psutil
"""Process and System Utilities
It can read:
CPU usage
RAM usage
Disk usage
Battery
Running processes
Network usage
Temperatures (on some systems)"""

from utils.logger import log_action


def system_info():

    print("\n==========================")
    print("    SYSTEM INFORMATION")
    print("==========================")

    # Operating System
    print(f"Operating System : {platform.system()} {platform.release()}")

    # Computer Name
    print(f"Computer Name    : {platform.node()}")

    # Processor
    print(f"Processor        : {platform.processor()}")

    # CPU Usage
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage        : {cpu}%")

    # RAM Information
    ram = psutil.virtual_memory()

    total_ram = round(ram.total / (1024 ** 3), 2)
    used_ram = round(ram.used / (1024 ** 3), 2)
    available_ram = round(ram.available / (1024 ** 3), 2)

    print("\nRAM")
    print("--------------------------")
    print(f"Used      : {used_ram} GB")
    print(f"Available : {available_ram} GB")
    print(f"Total     : {total_ram} GB")
    print(f"Usage     : {ram.percent}%")

    # Disk Information
    print("\nDISK USAGE")
    print("--------------------------")

    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            total = round(usage.total / (1024 ** 3), 2)
            used = round(usage.used / (1024 ** 3), 2)
            percent = usage.percent

            print(f"{partition.device}")
            print(f"Used : {used} GB / {total} GB ({percent}%)")
            print()

        except PermissionError:
            continue

    # Battery
    battery = psutil.sensors_battery()

    print("BATTERY")
    print("--------------------------")

    if battery:
        print(f"Level  : {battery.percent}%")

        if battery.power_plugged:
            print("Status : Charging")
        else:
            print("Status : Not Charging")
    else:
        print("Battery information not available.")

    print("==========================")

    log_action("Viewed System Information")
