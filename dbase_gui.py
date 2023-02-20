from time import time, ctime
from os.path import exists, abspath, join, split as splitdir
from hashlib import md5


PATH: str = r'c:\Users\lavro\Desktop\ProCoding\python_scripts\vsblue\baza.txt'
SUPER_USER: int = 0
CODE_POS: int = 1
CODE_EXIT: int = 2
CODE_NEG: int = 0
POS_ANW: tuple = ("yes", "sure", "ye", "yeah")
NEG_ANW: tuple = ("no", "nah")
FILEPATH: str = abspath(__file__)
DIRNAME, FILENAME = splitdir(FILEPATH)
DB_FILE_NAME: str = r"baza.txt"
SEPTAB: str = "\t" * 7
ORGPOL: tuple = (
    "ID", "LOGIN", "PASSWORD",
    "NAME", "SURNAME", "AGE",
    "NICKNAME", "LSO", "ROLE"
)
ROLES: tuple = (
    "User", "Admin"
)

db: list = []


def hash(string: str) -> str:
    '''Encrypts data.'''
    h_str = md5(bytes(string, "utf-8"))
    return h_str.hexdigest()


def user_answer(
    question: str,
    posanswer: tuple=POS_ANW,
    neganswer: tuple=NEG_ANW,
    notification: str=""
) -> int:
    '''Asks user a question and returns bool depending on answer.'''
    answ: str = ""
    if notification:
        print(notification)
    while answ not in posanswer + neganswer:
        answ = input(question).strip().lower()
        if answ in posanswer:
            return CODE_POS
        elif answ in neganswer:
            return CODE_NEG
        else:
            print("We did not understand you")
            print(
                "Please use answers presented: POSITIVES: "
                f"({', '.join(posanswer)}) or NEGATIVES: "
                f"({', '.join(neganswer)})"
            )


def read_row(string: str) -> tuple:
    '''Returns fields for database.'''
    return tuple(map(str.strip, string.split(SEPTAB)))


def load_dbase() -> list:
    '''Loads database in the code.'''
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


def list_to_strtab(row: list) -> str:
    '''Makes string made of database fields.'''
    return SEPTAB.join(map(str, tuple(row)))


def save_dbase(dbase: list) -> None:
    '''Saves database.'''
    log_front: str = list_to_strtab(dbase[0].keys())
    with open(PATH, "wt", encoding="utf-8") as file_save:
        print(log_front, file=file_save)
        for row in dbase:
            print(list_to_strtab(row.values()), file=file_save)


def identification(role: str="User") -> list:
    '''Adds new user to database.'''
    global db
    user_model: dict = {}
    user_model["ID"] = str(int(db[-1]["ID"]) + 1)
    for i in tuple(db[0].keys())[1:-2]:
        if i == "PASSWORD":
            user_model[i] = hash(input(f"Type in new <{i}>: "))
        else:
            user_model[i] = input(f"Type in new <{i}>: ")
    user_model["LSO"] = ctime(time())
    user_model["ROLE"] = role
    db.append(user_model)


def user_delete(userid: int) -> None:
    '''Deletes user from database.'''
    if str(userid) == str(SUPER_USER):
        print("Cannot delete this user.")
    else:
        global db
        list_id: list = tuple(map(lambda x: x["ID"], db))
        if userid in list_id:
            del db[list_id.index(userid)]
        else:
            print("Cannot find user with this ID.")


def user_reg() -> None:
    '''Menu.'''
    request: str = ""
    P_S, P_L, P_C, P_E = range(1, 5)
    MENU_OPTS: dict = {
        str(P_S): "Sign in",
        str(P_L): "Log in",
        str(P_C): "Contact support",
        str(P_E): "Exit",
    }
    OPT_FUNC: dict = {
        "Sign in": identification,
        "Log in": 1,
        "Contact support": 2,
        "Exit": 3,
    }
    print("\nMenu:\n\n")
    for key, value in sorted(MENU_OPTS.items()):
        print(f"\t{key} : {value}\n")
    print("\n\n")
    while request not in (tuple(MENU_OPTS.keys()) +tuple(MENU_OPTS.values())):
        request = input("Chose option: ").strip().capitalize()
        if request in MENU_OPTS.keys():
            OPT_FUNC[MENU_OPTS[request]]()
        elif request in MENU_OPTS.values():
            OPT_FUNC[request]()
        else:
            print("Task is unknown.")


def create_db() -> None:
    '''Creates new database.'''
    if user_answer(
        "Would you like to create the database file in the same directory?: "
    ):
        path: str = join(DIRNAME, DB_FILE_NAME)
    else:
        path: str = join(input(
            "Where would you like to create database: "
            ), DB_FILE_NAME
        )
    with open(FILEPATH, "rt", encoding="utf-8") as pathchange:
        oldfile: list = pathchange.readlines()
    for index in range(len(oldfile)):
        if "PATH: str = " in oldfile[index]:
            oldfile[index] = f"PATH: str = r'{path}'\n"
            break
    with open(FILEPATH, "wt", encoding="utf-8") as writing:
        print(*oldfile, sep="", end="", file=writing)
    with open(path, "wt", encoding="utf-8") as new_file:
        print("", end="", file=new_file)
    #fill_db()
    print(
        "New path for your database is made, "
        "restart the application to continue"
    )


def fill_db() -> None:
    '''Fills empty database and adds sviser.'''
    userdata: list = [0, ]
    print("\n\n\tSuper user identification: \n\n")
    for field in ORGPOL[1:-2]:
        if field == "PASSWORD":
            userdata.append(hash(input(f"Type in new <{field}>: ")))
        else:
            userdata.append(input(f"Type in new <{field}>: "))
    userdata.append(ctime(time()))
    userdata.append("Admin")
    with open(PATH, "wt", encoding="utf-8") as filldb:
        print(list_to_strtab(ORGPOL), file=filldb)
        print(list_to_strtab(userdata), file=filldb)


def checkbase(code: int=CODE_NEG) -> int:
    '''Checks if database exists.'''
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
        return CODE_NEG
    with open(PATH, "rt", encoding="utf-8") as checkfile:
        data: list = checkfile.readlines()
        if not data or len(data) <= 1:
            if user_answer(
                "Do you want to fill in the database?: ",
                notification="Databse is empty"
            ):
                fill_db()
                return CODE_POS
            else:
                print("Database fill declined")
            fill_db()
            return CODE_POS
        else:
            print("Database loaded sucsessfully.")
            return CODE_POS


def main():
    '''Main program cycle.'''
    if checkbase():
        global db
        try:
            db = load_dbase()
            save_dbase(db)
        except ValueError:
            checkbase(code=CODE_POS)
        except KeyError:
            checkbase(code=CODE_POS)
        #user_reg()
        #identification()
        #user_delete()
    else:
        print("Programm ended sucsessfully")


if __name__ == "__main__":
    main()
