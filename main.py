from os.path import abspath
from dbase_func.creation import *
from const import CODE_LANG, UNKNOWN
from localise_func.interact_user import get_code


FILEPATH: str = abspath(__file__)


def main():
    '''Main program cycle.'''
    code_language: int = get_code()
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