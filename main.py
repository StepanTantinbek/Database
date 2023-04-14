from os.path import abspath
from dbase_func.creation import load_dbase
from dbase_func.console import checking_settings
from interact_funcs.user import menu_authorization
from sys import argv


FILEPATH: str = abspath(__file__)


def main():
    '''Main program cycle.'''
    checking_settings(argv)
    db: dict = load_dbase()
    db, id = menu_authorization(db)
    #svae_dbase(db)
    print(db)

if __name__ == "__main__":
    main()