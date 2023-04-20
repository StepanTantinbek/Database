

'''includes functions to format data input by user for obtainment.'''


def perfect_dt(data: str) -> str:
    '''removes space chars and lowers all capital letters.'''
    return data.strip().lower()


def read_row(string: str) -> tuple:
    '''makes a list of data that user has to input.'''
    from data.const import SEPTAB
    return tuple(map(str.strip, string.split(SEPTAB)))

def get_str_for_record_db(row: __import__("typing").Union[list, tuple]) -> str:
    '''makes string with data types for user to put fot the database file.'''
    return __import__("data.const").SEPTAB.join(map(str, tuple(row)))

def get_str_for_record_db(user_data: dict) -> str:
    from data.const import SEPTAB
    tuple_from_dict: tuple = tuple(user_data.values())
    return get_str_for_record_db(tuple_from_dict)


def get_str_for_record_db(
        object: __import__('typing').Union[list, tuple, dict]
    ) -> str:
    if type(object) is dict:
        object =  tuple(object.values())
    return __import__('data').const.SEPTAB.join(map(str,object))


