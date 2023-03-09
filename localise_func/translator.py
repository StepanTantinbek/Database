

'''Includes localised function of translator function.'''


from typing import Callable


def lang_print_gen(main_lang: int) -> Callable[[str], None]:
    '''Generator of localisation translator function.'''
    from data.lang_pack import VOCAB
    TUPLE_NUMERATION_CONV: int = 1
    def lang_print(word: str) -> None:
        '''Prints phrase in chosen language.'''
        print(VOCAB[word][int(main_lang) - TUPLE_NUMERATION_CONV])
    return lang_print
