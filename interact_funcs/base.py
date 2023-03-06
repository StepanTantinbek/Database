

'''includes functions to format data input by user for obtainment.'''


from const import SEPTAB


def perfect_dt(data: str) -> str:
    '''removes space chars and lowers all capital letters.'''
    return data.strip().lower()


def read_row(string: str) -> tuple:
    '''makes a list of data that user has to input.'''
    return tuple(map(str.strip, string.split(SEPTAB)))

def list_to_strtab(row: list) -> str:
    '''makes string with data types for user to put fot the database file.'''
    return SEPTAB.join(map(str, tuple(row)))