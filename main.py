from os.path import abspath
from dbase_func.creation import load_dbase, save_dbase
from dbase_func.console import checking_settings
from interact_funcs.user import menu_authorization
from sys import argv
from models.user_model import User


FILEPATH: str = abspath(__file__)


def main():
    '''Main program cycle.'''
    checking_settings(argv)
    db: dict = load_dbase()
    db, id = menu_authorization(db)
    #print(db)
    active_user: User = User(id, db[id])
    active_user.add_new_friends(4)
    active_user.save()
    if not save_dbase(db):
        print("Database was not saved due to unknown eror")


if __name__ == "__main__":
    main()