

'''includes functions to modify database.'''


def create_user(id: int, role = "User") -> dict:
    from data.const import ORGPOL
    from verification_funcs.password import checkpssw
    from datetime import datetime
    new_user: dict = {}
    new_user["ID"] = id
    for field in ORGPOL[1:-2]:
        if field == "PASSWORD":
            new_user['PASSWORD'] = hash(checkpssw   )
        else:
            new_user[field] = input(f"Type in new <{field}>: ")
    new_user["LSO"] = datetime.now()
    new_user["ROLE"] = role
    return new_user


def registration(database: dict) -> tuple[dict, int]:
    '''adds new user to database.'''
    new_user_id: int = max(map(int, list(database.keys()))) + 1
    new_user: dict = create_user(new_user_id)
    return new_user

def user_delete(userid: int) -> None:
    '''deletes user from database.'''
    from data.const import SUPER_USER
    if str(userid) == str(SUPER_USER):
        print("Cannot delete this user.")
    else:
        global db
        list_id: list = tuple(map(lambda x: x["ID"], db))
        if userid in list_id:
            del db[list_id.index(userid)]
        else:
            print("Cannot find user with this ID.")


def filepath(dirfile: str, filename: str) -> str:
    '''Creates file in directory from file variable
    and name from second variable.'''
    from os.path import split as splitdir, join as joindir
    DIRINDX: int = 0
    dirname: str = splitdir(dirfile)[DIRINDX]
    finalpath: str = joindir(dirname, filename)
    return finalpath
