

'''This file contains functions needed for checking
and encrypting password and login.'''


from hashlib import md5
from ..interact_funcs.user import notification


PASS_LEN_MIN: int = 5


def hash(string: str) -> str:
    '''Encrypts data.'''
    h_str = md5(bytes(string, "utf-8"))
    return h_str.hexdigest()

def lencheck(passw: str, min_len: int=PASS_LEN_MIN) -> bool:
    '''Check data length.'''
    return notification(
        len(passw) >= min_len,
        neg=f"Password should be longer than {PASS_LEN_MIN - 1}"
    )