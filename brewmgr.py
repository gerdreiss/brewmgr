import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print_help()

    arg = sys.argv[1]
    if arg == "deps":
        elms = subprocess.check_output(["brew", "list"]).split('\n')
        print("looking to cleanup from the list\n{}".format(", ".join(elms)))
        for elm in elms:
            if elm != "":
                print("checking usage of {}".format(elm))
                deps = subprocess.check_output(["brew", "uses", "--installed", elm]).split('\n')
                if "".join(deps) == "":
                    remove = raw_input("nothing is using {}. uninstall? (N/y)".format(elm))
                    if remove == "y":
                        subprocess.call(["brew", "uninstall", elm])
                    else:
                        print("continuing...")
                else:
                    print("{} is used by {}. continuing...".format(elm, ", ".join(deps)))
            else:
                print("cleaning up...")
                subprocess.call(["brew", "cleanup"])
                print("done.")

    else:
        print_help()


def print_help():
    print("Usage: brewmgr deps")


if __name__ == "__main__":
    main()