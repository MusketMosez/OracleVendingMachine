from cmd import Cmd
import sys

floatChange = 0.0


class CmdSubclass(Cmd):

    def do_init(self, arg):
        """ Command to initialise"""
        global floatChange
        floatChange = float(arg)

    def do_printfloat(*args):
        """Help text for export"""
        print(floatChange)

    def do_exit(*args):
        return -1


if __name__ == '__main__':
    c = CmdSubclass()
    command = ' '.join(sys.argv[1:])
    if command:
        sys.exit(c.onecmd(command))
    c.cmdloop()




