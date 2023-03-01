

'''This file contains fucntions that format data.'''


SEPTAB: str = "\t" * 7


def perfect_dt(data: str) -> str: return data.strip().lower()


def read_row(string: str) -> tuple:
    '''Returns fields for database.'''
    return tuple(map(str.strip, string.split(SEPTAB)))

def list_to_strtab(row: list) -> str:
    '''Makes string made of database fields.'''
    return SEPTAB.join(map(str, tuple(row)))