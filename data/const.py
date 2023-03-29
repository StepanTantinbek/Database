from os.path import abspath
from os.path import split as dirsplit, join as dirjoin

CONSTPATH: str = abspath(__file__)
DIRINDX: int = 0
dirbase = dirsplit(CONSTPATH)[DIRINDX]
BASEPATH: str = dirjoin(dirbase, "const.py")
UNKNOWN: int = -1
CODE_LANG: int = 1
SUPER_USER: int = 0
PATH: str = r''
SEPTAB: str = "\t" * 7
PASS_LEN_MIN: int = 5
MAX_RPT_CHR: int = 5


POS_ANW: tuple = (
    "yes",
    "sure",
    "ye",
    "yeah",
    'y',
    'да',
    'д',
    'si',
)

NEG_ANW: tuple = (
    "no",
    "nah"
    'nope',
    'n',
    'нет',
    'н',
)


DB_FILE_NAME: str = r"baza.txt"


ORGPOL: tuple = (
    "ID",
    "LOGIN",
    "PASSWORD",
    "NAME",
    "SURNAME",
    "AGE",
    "NICKNAME",
    "LSO",
    "ROLE",
)


ROLES: tuple = (
    "User",
    "Admin",
)