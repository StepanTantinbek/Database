from os.path import abspath
from dbase_func.creation import checkbase, load_dbase, save_dbase
from localise_func.translator import localized_print
from dbase_func.console import checking_settings
from sys import argv


FILEPATH: str = abspath(__file__)


def main():
    '''Main program cycle.'''
    checking_settings(argv)
    if checkbase():
        try:
            db: list = load_dbase()
        except (ValueError, KeyError):
            checkbase(code=True)
        ...
        save_dbase(db)
    else:
        localized_print("Programm ended sucsessfully")


if __name__ == "__main__":
    main()