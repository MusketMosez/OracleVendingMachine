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
            if pounds > 20:
                userCoins['20'] += math.floor(pounds/20)
                pounds -= (math.floor(pounds/20) * 20)
            if 10 < pounds < 20:
                userCoins['10'] += 1
                pounds -= 10
            if 5 < pounds < 10:
                userCoins['10'] += 1
                pounds -= 5
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
            if float(key) >= 1:
                print('£' + key + ' X ' + str(int(coins[key])))
            else:
                if key[2] != '0':
                    print(key[2:] + 'p ' + 'X ' + str(int(coins[key])))
                else:
                    print(key[3:] + 'p ' + 'X ' + str(int(coins[key])))


def sum_dict(change):
    sum = 0
    for key in change.keys():
        sum += float(key) * change[key]
    return sum


# class contains call functions for API
class CmdSubclass(Cmd):

    def __init__(self):
        self.floatChange = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0,
                            '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}

        self.userCoins = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0,
                          '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}

        self.changeDue = {'20': 0, '10': 0, '5': 0, '2': 0, '1': 0, '0.50': 0,
                          '0.20': 0, '0.10': 0, '0.05': 0, '0.01': 0}

        self.remChange = {}

        self.floatSum = 0.0
        self.currentCost = 0.0
        self.paidAmount = 0.0
        self.hasSelected = False
        self.hasPurchased = False
        self.changePaid = True

        super(CmdSubclass, self).__init__()

    def do_init(self, arg):
        """ Command to initialise float amount for vending machine\n Usage: init [float] {int}"""
        usage = 'Usage: init [float]'
        allowed = [20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.05, 0.2, 0.1, 0.02, 0.01]
        arg = arg.split(' ')
        try:
            float(arg[0])
            if float(arg[0]) < 0:
                raise ValueError
            if float(arg[0]) not in allowed:
                raise ValueError
        except ValueError:
            print("ValueError: Initialise vending machine with legal tender as float and integer amount\n")
            print(usage + '\n')
            print('Accepted notes and coins:'
                  '£20, £10, £5,'
                  '£2, £1, 50p,'
                  '20p, 10p, 5p, 2p, 1p')
        else:
            for key in self.floatChange.keys():
                if float(str(key)) == float(arg[0]):
                    if len(arg) == 2:
                        amount = arg[1]
                        try:
                            amount = int(amount)
                        except ValueError:
                            print("ValueError: Amount should be integer value")
                        else:
                            self.floatChange[key] += amount
                    else:
                        self.floatChange[key] += 1
                    if not self.changePaid:
                        if key in self.remChange.keys():
                            self.remChange[key] = self.floatChange[key]


            if not self.changePaid:
                isZero = False
                for key in self.remChange:
                    if self.remChange[key] < 0:
                        isZero = True
                        print("Add {} more £{} to receive change".format(str(-1 * int(self.remChange[key])), str(key)))
                if not isZero:
                    self.do_getchange('')
                    self.changePaid = True

    def do_fastinit(self,arg):
        """Command to initialise float with default set of notes and coins\nUsage: fastinit"""
        usage = 'Usage: fastinit'
        self.floatChange = {'20': 5, '10': 5, '5': 5, '2': 5, '1': 5, '0.50': 5,
                            '0.20': 5, '0.10': 5, '0.05': 5, '0.01': 5}
        self.floatSum = sum_dict(self.floatChange)

    def do_buy(self, arg):
        """Command to purchase item for a specified price\n Usage: buy [float]"""
        usage = 'Usage: buy [float]'
        self.floatSum = sum_dict(self.floatChange)
        if self.floatSum <= 0:
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
        self.floatSum = sum_dict(self.floatChange)
        if self.floatSum <= 0:
            print('No float cast in machine, insert more float change using the init command')
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
                        if difference > self.floatSum:
                            print("Not enough float to provide change")
                        else:

                            self.currentCost -= (self.paidAmount - difference)
                            self.changeDue = parse_coins(difference, self.changeDue)
                            self.floatChange = {key: self.floatChange[key]-self.changeDue[key]
                                                for key in self.floatChange}
                            for key in self.floatChange:
                                if self.floatChange[key] < 0:
                                    self.remChange[key] = self.floatChange[key]
                                    # print(self.floatChange[key])
                                    self.changePaid = False
                                    print("Please enter more £{} to float to receive change".format(key))
                                else:
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

        self.floatSum = sum_dict(self.floatChange)
        print_coins(self.floatChange)
        print('Total Float: ' + "£{:,.2f}".format(self.floatSum))

    def do_getchange(self,arg):
        """"Command to receive change due\nUsage: getchange"""
        usage = 'Usage :getchange'
        if arg:
            print("Argument not required")
            print(usage)
        print('Change due: ' + "£{:,.2f}".format(self.changeDue))
        print_coins(self.changeDue)
        self.changeDue = dict.fromkeys(self.changeDue, 0)

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




