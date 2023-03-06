

'''includes functions to modify database.'''


from verification_funcs.password import ceckpssw
from verification_funcs.auxiliary import hash
from time import time, ctime
from const import SUPER_USER


def identification(role: str="User") -> list:
    '''adds new user to database.'''
    global db
    user_model: dict = {}
    user_model["ID"] = str(int(db[-1]["ID"]) + 1)
    for i in tuple(db[0].keys())[1:-2]:
        if i == "PASSWORD":
            user_model[i] = hash(ceckpssw())
        else:
            user_model[i] = input(f"Type in new <{i}>: ")
    user_model["LSO"] = ctime(time())
    user_model["ROLE"] = role
    db.append(user_model)


def user_delete(userid: int) -> None:
    '''deletes user from database.'''
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
    '''menu of what user is able to do.'''
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