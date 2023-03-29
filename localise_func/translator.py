

'''Includes localised function of translator function.'''

from localise_func.interact_user import get_code
from typing import Callable


def get_localized_print(code: int = 0) -> Callable[[str], None]:
    '''Generator of localisation translator function.'''
    from data.lang_pack import VOCAB
    TUPLE_NUMERATION_CONV: int = 1
    language_code: int
    if not code:
        language_code = get_code()
    else:
        language_code = code
    def lang_print(word: str, end = '\n') -> None:
        '''Prints phrase in chosen language.'''
        try:
            context: str = VOCAB[word][ language_code - TUPLE_NUMERATION_CONV]
        except KeyError:
            context: str = word
        except:
            print("Unknown error occured with translation")
        print(context, end = end)
    return lang_print

localized_print: Callable[[str], str] = get_localized_print()
