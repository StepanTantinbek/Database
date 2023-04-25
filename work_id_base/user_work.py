def lookup_user(
        id: __import__("typing").Union[int, str]
    ) -> int:
    from data.const import (
        CODE_USER_EXISTS,
        CODE_USER_NON_EXISTS,
        DATABASE_NON_EXISTS,
        UNKNOWN_ERROR,
        RELATIONPATH
    )
    from os.path import exists
    try:
        if exists(RELATIONPATH):
            with open(RELATIONPATH, "rt", encoding="utf-8") as readfile:
                readfile.readline()
                for line in readfile:
                    if line.startswith(f"{str(id)} "):
                        return CODE_USER_EXISTS
                return CODE_USER_NON_EXISTS
        return DATABASE_NON_EXISTS
    except:
        print("error")
        return UNKNOWN_ERROR