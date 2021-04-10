# argparse library provides command line interface (CLI)
import argparse

import sys
import os


# dictionary (hash table to store change)



# API functions
def init_vending_machine():
    if len(sys.argv) < 3:
        print(InitVendParser.print_usage())

# Create Parser
parser = argparse.ArgumentParser(prog='vend',
                                 description='operate Vending Machine',
                                 )

# add subparsers for sub commands
subparsers = parser.add_subparsers()

InitVendParser = subparsers.add_parser('init',
                                       help='initialise vending machine with float value',
                                       usage='init [float]')
InitVendParser.add_argument('float', type=float)
InitVendParser.set_defaults(func=init_vending_machine)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

args = parser.parse_args()
args.func()
