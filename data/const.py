from os.path import abspath
from dbase_func.data_work import filepath


CONSTPATH: str = abspath(__file__)
PATH: str = r'c:\Users\lavro\Desktop\ProCoding\python_scripts\vsblue\database_git\Database\baza.txt'
CONSTFILENAME: str = "const.py"
DIRINDX: int = 0
BASEPATH: str = filepath(CONSTPATH, CONSTFILENAME)
RELATIONPATH: str = r"C:\Users\lavro\Desktop\ProCoding\python_scripts\vsblue\database_git\Database\baza_relations.txt"

CODE_USER_EXISTS: int = 1
CODE_USER_NON_EXISTS: int = 2
DATABASE_NON_EXISTS: int = 3
UNKNOWN_ERROR: int = 4

UNKNOWN: int = -1
CODE_LANG: int = 2
SUPER_USER: int = 0
PASS_LEN_MIN: int = 5
MAX_RPT_CHR: int = 5

SEPTAB: str = "\t" * 7
SPACE: str = " "
SEPTAB_SPACES = SPACE * 25
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

ORGPOL_RELATIONS: tuple[str] = (
    "ID_USER",
    "ID_FRIENDS",
    "ID_CHAT"
)

ORGPOL_MSG: tuple[str] = (
    "HASH_KEY_ID",
    "ID_INTERLOCATOR",
    "TEXT",
    "DATE",
    "IS_SEEN"
)

ROLES: tuple = (
    "User",
    "Admin",
)