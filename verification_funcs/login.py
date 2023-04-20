

'''(BEING DEVELOPED)includes functions to work with users login.'''

def checklog(login: str, database: dict) -> bool:
    user_data_without_id: tuple[dict] = tuple(database.values())
    logins: tuple[str] = tuple(
        map(
            lambda data: data["LOGIN"],
            user_data_without_id
        )
    )
    return login in logins
