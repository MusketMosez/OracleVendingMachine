import math
from cmd import Cmd
import sys


# helper functions

# changes sum of money into change
def parse_coins(coins, userCoins):

    # separate pounds from change
    pounds = math.floor(coins)
    smallChange = coins - pounds

    # add the number of £1 and £2 coins to dictionary
    if pounds != 0:
        if pounds == 1:
            userCoins['1'] += 1
        else:
            if pounds % 2 == 0:
                userCoins['2'] += pounds/2
            else:
                userCoins['1'] += 1
                userCoins['2'] += (pounds - 1) / 2



    # add the number of 50p, 20p, 10p, 5p and 1p to dictionary
    fifties, smallChange = divmod(smallChange, 0.50)
    twenties, smallChange = divmod(smallChange, 0.20)
    tens, smallChange = divmod(smallChange, 0.10)
    fives, smallChange = divmod(smallChange, 0.05)
    pennies = round(smallChange / 0.01, 0)

    userCoins['0.50'] += fifties
    userCoins['0.20'] += twenties
    userCoins['0.10'] += tens
    userCoins['0.05'] += fives
    userCoins['0.01'] += pennies

    return userCoins


# prints dictionary of coins in readable format
def print_coins(coins):
    for key in coins.keys():
        if coins[key] != 0:
            if len(key) != 1:
                if key[2] != '0':
                    print(key[2:] + 'p ' + 'X ' + str(int(coins[key])))
                else:
                    print(key[3:] + 'p ' + 'X ' + str(int(coins[key])))
            else:
                print('£' + key + ' X ' + str(int(coins[key])))


# class contains call functions for API
class CmdSubclass(Cmd):

    def __init__(self):
        self.floatChange = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
        self.currentCost = 0.0
        self.paidAmount = 0.0
        self.hasSelected = False
        self.hasPurchased = False
        self.userCoins = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
        self.changeDue = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
        super(CmdSubclass, self).__init__()

    def do_init(self, arg):
        """ Command to initialise float amount for vending machine\n Usage: init [float]"""
        usage = 'Usage: init [float]'
        try:
            self.floatChange = float(arg)
            if float(arg) < 0:
                raise ValueError

        except ValueError:
            print("ValueError: Initialise vending machine with positive float value")
            print(usage)

    def do_buy(self, arg):
        """Command to purchase item for a specified price\n Usage: buy [float]"""
        usage = 'Usage: buy [float]'
        if self.floatChange <= 0:
            print('Insert more float change using the init command')
        else:
            try:
                self.currentCost += float(arg)
                if float(arg) < 0:
                    raise ValueError
            except ValueError:
                print('ValueError: Enter positive float value as cost of item')
                print(usage)
            else:
                self.hasSelected = True

    def do_deposit(self, arg):
        """Command to purchase item for a specified price\n Usage: buy [float]"""
        usage = 'Usage: buy [float]'
        if self.floatChange <= 0:
            print('Insert more float change using the init command')
        else:
            if self.hasSelected is True and self.currentCost > 0.0:
                try:
                    self.paidAmount += float(arg)
                    if float(arg) < 0:
                        raise ValueError
                except ValueError:
                    print('ValueError: Deposit positive float value')
                    print(usage)
                else:
                    self.userCoins = parse_coins(float(arg), self.userCoins)
                    print('Current cost of selection: ' + "£{:,.2f}".format(self.currentCost))
                    print('Deposited amount: ' + '£' + str(arg))
                    print('Total Deposit: ' + "£{:,.2f}".format(self.paidAmount))
                    difference = self.paidAmount - self.currentCost
                    if difference < 0:
                        print('Deposit more money, amount required: ' + "£{:,.2f}".format(difference * -1))
                    else:
                        print('Change due: ' + "£{:,.2f}".format(difference))
                        self.floatChange -= difference
                        self.changeDue = parse_coins(difference, self.changeDue)
                        self.currentCost -= (self.paidAmount - difference)
                        self.userCoins = dict.fromkeys(self.userCoins, 0)
                        self.paidAmount = 0.0
                        self.hasSelected = False
            else:
                print('Make a selection using buy command')

    def do_getfloat(self, arg):
        """Command to print current vending machine float amount\nUsage: getfloat"""
        usage = 'Usage: getfloat'
        if arg:
            print("Argument not required")
            print(usage)
        print("£{:,.2f}".format(self.floatChange))

    def do_getchange(self,arg):
        """"Command to receive change due\nUsage: getchange"""
        usage = 'Usage :getchange'
        if arg:
            print("Argument not required")
            print(usage)
        print_coins(self.changeDue)

    def do_getdeposit(self, arg):
        """Command to receive the total amount currently\ndeposited by user with option to recieve amount in change format\nUsage: getdeposit {change} """
        usage = 'Usage: getdeposit {change}'
        if arg:
            if arg == 'change':
                print_coins(self.userCoins)
            else:
                print(' To receive amount in change format enter: "getdeposit change" ')
        else:
            print("£{:,.2f}".format(self.paidAmount))

    def do_getcost(self, arg):
        """Command to receive cumulative cost of all selections\nUsage: getcost """
        usage = 'Usage: getcost'
        if arg:
            print("Argument not required")
            print(usage)
        print("£{:,.2f}".format(self.currentCost))

    def do_test(self, arg):
        print(type(arg.split(' ')))

    def do_exit(*args):
        return -1


if __name__ == '__main__':

    c = CmdSubclass()
    command = ' '.join(sys.argv[1:])
    if command:
        sys.exit(c.onecmd(command))
    c.cmdloop()




