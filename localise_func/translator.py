

'''Includes localised function of translator function.'''


from typing import Callable


def lang_print_gen(main_lang: int) -> Callable[[str], None]:
    '''Generator of localisation translator function.'''
    TUPLE_NUMERATION_CONV: int = 1
    def lang_print(word: str) -> None:
        '''Prints phrase in chosen language.'''
        vocab: dict = {
            "Programm ended sucsessfully": (
            "Programm ended sucsessfully",
            "Programma zavershena uspeshno",
            "Le programme endo sucsesion"
            )
        }
        print(vocab[word][int(main_lang) - TUPLE_NUMERATION_CONV])
    return lang_print