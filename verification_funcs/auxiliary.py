

'''includes functions to work with users personal data.'''


def hash(string: str) -> str:
    '''encrypts data.'''
    from hashlib import md5
    h_str = md5(bytes(string, "utf-8"))
    return h_str.hexdigest()


def lencheck(passw: str, min_len: int=0) -> bool:
    '''checks string length.'''
    from interact_funcs.user import notification
    from data.const import  PASS_LEN_MIN
    if not min_len:
        min_len = PASS_LEN_MIN
    return notification(
        len(passw) >= min_len,
        neg=f"Password should be longer than {PASS_LEN_MIN - 1}"
    )