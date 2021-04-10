from cmd import Cmd
import sys




class CmdSubclass(Cmd):

    def __init__(self):
        self.floatChange = 0.0
        self.currentCost = 0.0
        self.hasSelected = False
        self.hasPurchased = False
        self.userCoins = {}
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

    def do_cost(self, arg):

        try:
            self.currentCost += arg
        except ValueError:
            print('ValueError: Enter float value as cost of item')
        self.hasSelected = True

    def do_buy(self, arg):
        if self.hasSelected == True and self.currentCost > 0.0:
            try:
                self.userCoins = parse_coins(arg)

    def do_test(self, arg):
        print(type(arg.split(' ')))


    # def do_purchase(self, arg):

    def do_exit(*args):
        return -1


if __name__ == '__main__':
    c = CmdSubclass()
    command = ' '.join(sys.argv[1:])
    if command:
        sys.exit(c.onecmd(command))
    c.cmdloop()




