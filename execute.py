#!/usr/bin/env python3

# Import Python packages
import glob
import json
import platform


def lookup_os():
    """gets OS info"""
    os_name = platform.system()
    return os_name


def command():
    """Finds directories in /Proc, reads their status, and excludes the rest"""
    status_pid = dict()
    for pid in glob.glob("/proc/*/status"):
        try:
            status_pid[pid] = open(pid).read()
        except:
            continue
    return status_pid


def format(proc):
    """formats data to JSON"""
    with open("output.json", "w") as write_file:
        json.dump(proc, write_file, indent=4)


def main():
    """Call Functions"""
    os_name = lookup_os()
    proc = command()

    # Only allows the program to continue if it is Linux.
    if "Linux" in os_name:
        format(proc)
    else:
        print(os_name, "is the wrong operating system!")


if __name__ == "__main__":
    main()
