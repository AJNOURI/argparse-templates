import sys
import argparse


class AlecorParser(argparse.ArgumentParser):
    """
    Handle special case and show help on invalid argument
    """
    def error(self, message):
        sys.stderr.write('\nERROR: {}\n\n'.format(message))
        self.print_help()
        sys.exit(2)

def main():
    pass

if __name__ == '__main__':

    try:

        parser = AlecorParser(epilog='v{}')
        parser.add_argument('-v', '--version', action='version', version='0.1')
        parser.add_argument('-l', '--log', metavar=('SAMPLE1'), help='1 var expected: SAMPLE1')
        parser.add_argument('-t', '--two', nargs=2, metavar=('VAR1', 'VAR2'), help='2 vars expected: VAR1 VAR2')
        parser.add_argument('-f', '--flag', action='store_true', help='Flag option (True/False)')
        parser.add_argument('-d', '--default', help='default behaviour var')
        args = parser.parse_args()

        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(0)

        if args.log:
            print(args.log)

        if args.flag:
            print(args.flag)
            main()

    except Exception, e:
        raise e