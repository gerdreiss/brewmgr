#!/usr/bin/python

import subprocess
import sys


def main():
    check_brew_installation()
    check_args(sys.argv)

    arg1 = sys.argv[1]

    if arg1 == "usage":
        output = subprocess.check_output(["brew", "list"])
        elms = output.split('\n')
        print("looking to cleanup from the list:\n{}".format("\n".join(elms)))

        for elm in elms:
            if elm == "":
                clean_up()

            else:
                check_usage(elm)

    else:
        print(help_message())
        sys.exit("unknown option: {}".format(arg1))


def check_usage(elm):
    print("checking usage of {}".format(elm))
    usage = subprocess.check_output(["brew", "uses", "--installed", elm])

    if usage == "":
        remove = raw_input("nothing is using {}. uninstall? (N/y)".format(elm))
        if remove == "y":
            subprocess.call(["brew", "uninstall", elm])

    else:
        print("{} is used by {}".format(elm, usage))


def check_brew_installation():
    output = subprocess.check_output(["which", "brew"])
    if output == "":
        sys.exit("Homebrew not installed.")


def check_args(args):
    if len(args) < 2:
        sys.exit(help_message())


def clean_up():
    print("cleaning up...")
    subprocess.call(["brew", "cleanup"])
    print("done.")


def help_message():
    return "Usage: brewmgr usage"


if __name__ == "__main__":
    main()
