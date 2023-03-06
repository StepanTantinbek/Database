

'''includes functions to create database.'''


from interact_funcs.user  import user_answer
from interact_funcs.base import list_to_strtab, read_row
from os.path import join, exists, split as splitdir
from time import time, ctime
from main import FILEPATH
from verification_funcs.password import checkpssw
from const import (
    DB_FILE_NAME,
    PATH,
    ROLES,
    ORGPOL,
    CONST_FILE_NAME
)

DIRNAME, FILENAME = splitdir(FILEPATH)


def create_db() -> None:
    '''creates database.'''
    if user_answer(
        "Would you like to create the database file in the same directory?: "
    ):
        path: str = join(DIRNAME, DB_FILE_NAME)
    else:
        path: str = join(input(
            "Where would you like to create database: "
            ), DB_FILE_NAME
        )
    CONST_PATH: str = join(DIRNAME, CONST_FILE_NAME)
    with open(CONST_PATH, "rt", encoding="utf-8") as pathchange:
        oldfile: list = pathchange.readlines()
    for index in range(len(oldfile)):
        if "PATH: str = " in oldfile[index]:
            oldfile[index] = f"PATH: str = r'{path}'\n"
            break
    with open(CONST_PATH, "wt", encoding="utf-8") as writing:
        print(*oldfile, sep="", end="", file=writing)
    with open(path, "wt", encoding="utf-8") as new_file:
        print("", end="", file=new_file)
    #fill_db()
    print(
        "New path for your database is made, "
        "restart the application to continue"
    )


def load_dbase() -> list:
    '''loads database to the code to work with it.'''
    user_model: dict = {}
    db = []
    with open(PATH, "rt", encoding="utf-8") as dbase:
        db_read: tuple = read_row(dbase.readline())
        for i in db_read:
            user_model[i] = ""
        for i in dbase.readlines():
            db.append(user_model)
            db[-1] = dict(zip(db_read, read_row(i)))
            if not all((
                (len(db[-1]) == 9),
                (db[-1]["ID"].isdigit()),
                (db[-1]["ROLE"] in ROLES)
            )):
                raise ValueError("Incorrect data in the database")
    return db


def save_dbase(dbase: list) -> None:
    '''uploads database to the main file.'''
    log_front: str = list_to_strtab(dbase[0].keys())
    with open(PATH, "wt", encoding="utf-8") as file_save:
        print(log_front, file=file_save)
        for row in dbase:
            print(list_to_strtab(row.values()), file=file_save)


def fill_db() -> None:
    '''if database is empty, it will add superviser, database ready.'''
    userdata: list = [0, ]
    print("\n\n\tSuper user identification: \n\n")
    for field in ORGPOL[1:-2]:
        if field == "PASSWORD":
            userdata.append(hash(checkpssw()))
        else:
            userdata.append(input(f"Type in new <{field}>: "))
    userdata.append(ctime(time()))
    userdata.append("Admin")
    with open(PATH, "wt", encoding="utf-8") as filldb:
        print(list_to_strtab(ORGPOL), file=filldb)
        print(list_to_strtab(userdata), file=filldb)


def checkbase(code: bool=False) -> bool:
    '''checks if database is exist or damaged.'''
    notification: str = ""
    if not exists(PATH) or code:
        if not code:
            notification = "Database does not exist"
        else:
            notification = "Database is damaged"
        if user_answer(
            "Do you want to create a new database?: ",
            notification=notification
        ):
            create_db()
        else:
            print("Database creation declined")
        return False
    with open(PATH, "rt", encoding="utf-8") as checkfile:
        data: list = checkfile.readlines()
        if not data or len(data) <= 1:
            if user_answer(
                "Do you want to fill in the database?: ",
                notification="Databse is empty"
            ):
                fill_db()
                return True
            else:
                print("Database fill declined")
            fill_db()
            return True
        else:
            print("Database loaded sucsessfully.")
            return True