from os.path import abspath
from dbase_func.data_work import filepath


CONSTPATH: str = abspath(__file__)
PATH: str = r''
CONSTFILENAME: str = "const.py"
DIRINDX: int = 0
BASEPATH: str = filepath(CONSTPATH, CONSTFILENAME)

UNKNOWN: int = -1
CODE_LANG: int = UNKNOWN
SUPER_USER: int = 0
PASS_LEN_MIN: int = 5
MAX_RPT_CHR: int = 5

SEPTAB: str = "\t" * 7
DB_FILE_NAME: str = r"baza.txt"

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