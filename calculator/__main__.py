import sys


def main(args=None):
    """The main routine"""
    if args is None:
        args = sys.argv[1:]

    print("This is a barebones calculator package")


if __name__ == "__main__":
    main()
