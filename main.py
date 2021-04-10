# argparse library provides command line interface (CLI)
import argparse

import sys
import os

# Create Parser
myParser = argparse.ArgumentParser(description='Operate Vending Machine')

args = myParser.parse_args()
