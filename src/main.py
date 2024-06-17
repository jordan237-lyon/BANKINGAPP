import sys
from terminale import run_terminale
from interface import run_interface
from database import Bank

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'terminale':
        run_terminale()
    else:
        run_interface()


if __name__ == "__main__":
    main()