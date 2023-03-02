from os.path import abspath
from dbase_func.creation import *


FILEPATH: str = abspath(__file__)


def main():
    '''Main program cycle.'''
    if checkbase():
        try:
            db: list = load_dbase()
        except (ValueError, KeyError):
            checkbase(code=True)
        ...
        save_dbase(db)
    else:
        print("Programm ended sucsessfully")


if __name__ == "__main__":
    main()