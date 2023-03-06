

'''includes functions to work with users personal data.'''


from const import  PASS_LEN_MIN
from hashlib import md5
from interact_funcs.user import notification


def hash(string: str) -> str:
    '''encrypts data.'''
    h_str = md5(bytes(string, "utf-8"))
    return h_str.hexdigest()

def lencheck(passw: str, min_len: int=PASS_LEN_MIN) -> bool:
    '''checks string length.'''
    return notification(
        len(passw) >= min_len,
        neg=f"Password should be longer than {PASS_LEN_MIN - 1}"
    )