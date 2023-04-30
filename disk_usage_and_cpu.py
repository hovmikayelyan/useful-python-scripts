#!/usr/bin/env python3
# @author hovmikayelyan
#
# This script allows us to check the CPU usage and disk free space automatically.
# You can change the amounts of checker functions below.
#
# Thank you!

import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")