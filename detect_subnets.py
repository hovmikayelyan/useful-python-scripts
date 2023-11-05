#!/usr/bin/env python3
import ipaddress
import os.path
import sys
import re

DEFAULT_INTERNAL_SUBNETS = ['10.254.196.0/24']
DEFAULT_EXTERNAL_SUBNETS = ['87.250.247.0/24']
INTERNAL_SUBNETS_FILE = 'internal_subnets.txt'
EXTERNAL_SUBNETS_FILE = 'external_subnets.txt'

ip_subnets = {"internal": [], "external": []}


def configure_subnets():
    if os.path.exists(INTERNAL_SUBNETS_FILE):
        with open(INTERNAL_SUBNETS_FILE) as internal_file:
            int_subnets = internal_file.read().split('\n')
            ip_subnets["internal"].extend(int_subnets)

    if os.path.exists(EXTERNAL_SUBNETS_FILE):
        with open(EXTERNAL_SUBNETS_FILE) as external_file:
            ext_subnets = external_file.read().split('\n')
            ip_subnets["external"].extend(ext_subnets)

    ip_subnets["internal"].extend(DEFAULT_INTERNAL_SUBNETS)
    ip_subnets["external"].extend(DEFAULT_EXTERNAL_SUBNETS)


def get_ip_subnet_type(ip):
    ip_obj = ipaddress.ip_address(ip)
    if any(ip_obj in ipaddress.ip_network(subnet) for subnet in ip_subnets['internal']):
        return 'internal'
    elif any(ip_obj in ipaddress.ip_network(subnet) for subnet in ip_subnets['external']):
        return 'external'
    else:
        return 'unknown'


def main():
    configure_subnets()
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        else:
            fields = line.split()
            pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

            match = re.search(pattern, line)
            if match:
                ip_address = match.group()
                subnet_type = get_ip_subnet_type(ip_address)
                fields.append(subnet_type)
                output_string = " ".join(fields)
                print(output_string)


if __name__ == "__main__":
    sys.exit(main())
