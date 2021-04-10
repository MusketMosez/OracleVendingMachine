import math
from cmd import Cmd
import sys


# helper functions
def parse_coins(coins, userCoins):

    pounds = math.floor(coins)
    smallChange = coins - pounds

    if pounds != 0:
        if pounds == 1:
            userCoins['1'] += 1
        else:
            if pounds % 2 == 0:
                userCoins['2'] += pounds/2
            else:
                userCoins['1'] += 1
                userCoins['2'] += (pounds - 1) / 2

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


class CmdSubclass(Cmd):

    def __init__(self):
        self.floatChange = 0.0
        self.currentCost = 0.0
        self.paidAmount = 0.0
        self.hasSelected = False
        self.hasPurchased = False
        self.userCoins = {'2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
        self.changeDue = {'2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
        super(CmdSubclass, self).__init__()

    def do_init(self, arg):
        """ Command to initialise float amount for vending machine\n Usage: init [float]"""
        usage = 'Usage: init [float]'

        try:
            self.floatChange = float(arg)
        except ValueError:
            print("ValueError: Initialise vending machine with float value")
            print(usage)

    def do_printfloat(self, arg):
        """Command to print current vending machine float value\nUsage: pc"""
        usage = 'Usage: pc'
        if arg:
            print("Argument not required")
            print(usage)
        print(self.floatChange)

    def do_buy(self, arg):
        try:
            self.currentCost += float(arg)
        except ValueError:
            print('ValueError: Enter float value as cost of item')
        self.hasSelected = True

    def do_deposit(self, arg):
        if self.hasSelected is True and self.currentCost > 0.0:
            self.paidAmount += float(arg)
            self.userCoins = parse_coins(self.paidAmount, self.userCoins)
            print('Current cost of selection: ' + '£' + str(self.currentCost))
            print('Deposited amount: ' + '£' + str(arg))
            difference = self.paidAmount - self.currentCost
            if difference < 0:
                print('Deposit more money, amount required: ' + str(round(difference, 2) * -1))
            else:
                print('Change due: ' + '£' + str(round(difference, 2)))
                self.changeDue = parse_coins(difference, self.changeDue)
                #print(self.changeDue)
                self.hasSelected = False
        else:
            print('Make a selection using buy command')


    def do_test(self, arg):
        print(type(arg.split(' ')))


    # def do_purchase(self, arg):

    def do_exit(*args):
        return -1


if __name__ == '__main__':
    temp_dict = {'2':0, '1': 0,'0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}
    parse_coins(12.77, temp_dict)
    c = CmdSubclass()
    command = ' '.join(sys.argv[1:])
    if command:
        sys.exit(c.onecmd(command))
    c.cmdloop()




