# OracleVendingMachine
Vending Machine written in Python

- The user can initialise the machine with coins that contribute to the float (change for transactions)

- The user can purchase items and specify the price

- The user can deposit cash to pay for items

- If change is due, the user will receive money from float

- The user can track amounts such as total cost of selection, total deposited cash and amount of float cash in machine

## Dependencies
1. Operating system: Linux/Windows Vista and newer/macOS Snow Leopard (macOS 10.6, 2008) and newer
2. Python 3.7
    * Download: https://www.python.org/downloads/release/python-370/
    * Terminal install for Linux
      
      `sudo apt install python3.7`

## Installation
- Download code from: https://github.com/MusketMosez/OracleVendingMachine
    * Alternatively use git from terminal/command line
      
      `git clone https://github.com/MusketMosez/OracleVendingMachine`

## Usage
- Using command prompt/terminal `cd` to OracleVendingMachine folder
    * For example:
    
      `cd C:\Users\user\workspace\OracleVendingMachine`

- From there, run the program using: `python main.py`
    * if `python` does not work, try `python3` instead

- This will then open up a shell on the command line where the user may enter commands

### Commands
- To receive list of commands type `help`
    * Help for specific command: `cmd help`
    
#### Float
- To use the vending machine, it must first be initialised with float change
  this can be acheived using two commands:
  
    * `init [pound] {amount}`
    
    * `fastinit`

- The `init` command takes a paramater `[pound]` and optional parameter `{amount}`
    * `init 20` places one £20 note in machine
    * `init 1 5` places five £1 coins in machine
    * `init 0.1 10` places ten 10p coins in machine
    
- The `fastinit` command initalises the float with five of each note/coin

- The user can inspect the float value at any point using:

      `getfloat`

#### Item Selection

- The user purchases an item by specifying a price using the buy command:
    * `buy [price]`
- To purchase an item worth 90p, the user would enter:
    * `buy 0.9`
    
 - The user can issue a series of `buy` commands before deciding to deposit money
 
 - The user can inspect the total cost using the `getcost` command

#### Depositing Money

- Before depositing money the user must have selected an item using the `buy` command

- After selection, the user can then deposit money using the deposit command:
    * `deposit [amount]`

- To deposit £2.50, the user would enter:
    * `deposit 2.5`

- If the deposited amount does not cover the total cost of selection the user will be asked to deposit more money

- To view the current deposited amount the `getdeposit` command can be used:
    * `getdeposit {change}`
    
- If the user had currently deposited three £1 coins then `getdeposit` would return £3.00

- If the user would like to view the deposited amount in change the optional parameter `change` can be used
    * e.g. `getdeposit change`

#### Receieving change

- If the user is due change after purchasing an item this amount can be attained using the `getchange` command

### Testing

- To run set of unit tests, execute the test script inside the directory folder
    * `python test_script.py`

## Notes

- Assumes user inserts full amount in one go e.g. £10.70 instead of 1 x £10 note, 1 x 50p and 1 x 20p

- Does not deduct optimal change from float e.g. if no 20p available deduct 2 x 10p instead

## Improvements to be made

- Separate some logic from class methods into helper functions to improve readability

- Provide default set of items and corresponding prices like a real vending machine

- Optimise change deducted from float

- Add complete checks in unit tests e.g. extreme bounds of input

- Make commands clearer/more concise e.g. get float  instead of getfloat

- Print outputs of change in nicer format using tables

