from os.path import abspath
from dbase_func.creation import *
from localise_func.interact_user import get_code
from localise_func.translator import lang_print_gen


FILEPATH: str = abspath(__file__)
code_lang: int


def main():
    '''Main program cycle.'''
    globals()["code_lang"] = get_code()
    print = lang_print_gen(code_lang)
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