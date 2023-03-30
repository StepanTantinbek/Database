

'''(BEING DEVELOPED)includes functions to work with users login.'''


from verification_funcs.auxiliary import lencheck


def logincheck(udatabase: list) -> str:
    LOG_COD_INX: int = 1
    logs: list = []
    for userinfo in udatabase:
        logs.append(userinfo[LOG_COD_INX])
    print(logs)
