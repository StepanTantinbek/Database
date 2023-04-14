

'''includes functions to interract with user.'''


from interact_funcs.base import perfect_dt
from data.const import POS_ANW, NEG_ANW


def notification(flag: bool, pos: str='', neg: str ='') -> bool:
    '''prints negative or positive comment depending on statement status.'''
    if flag and pos:
        print(pos)
    elif not flag and neg:
        print(neg)
    return flag


def user_answer(
    question: str,
    posanswer: tuple=POS_ANW,
    neganswer: tuple=NEG_ANW,
    notification: str=""
) -> int:
    '''asks user a question and returns result depending on answer.'''
    from localise_func.translator import localized_print
    answ: str = ""
    if notification:
        localized_print(notification)
    while answ not in posanswer + neganswer:
        localized_print(question, end ='')
        answ = perfect_dt(input())
        if answ in posanswer:
            return True
        elif answ in neganswer:
            return False
        else:
            localized_print("We did not understand you")
            localized_print("Please use answers presented: POSITIVES: ", end ='')
            print(', '.join(posanswer) ,end = ' ')
            localized_print("or NEGATIVES: ")
            print(', '.join(neganswer))

        
def menu_authorization(database: dict) -> tuple[dict, int]:
    '''Menu algorithm for user to use.'''
    from typing import Callable
    def log_in() -> int:
        ...
    def sign_up() -> int:
        ...
    def settings() -> None:
        ...
    def contact_us() -> str:
        ...
    MENU_ACTS: dict[str, str] = {
        '1': 'Log in',
        '2': 'Sign up',
        '3': 'Settings',
        '4': 'Contact us',
        '5': 'Exit',
    }
    ACTS_FUNCS: dict[str, Callable[[], Union[str, int, None]]] = {
        'Log in': log_in(),
        'Sign up': sign_up(),
        'Settings': settings(),
        'Contact us': contact_us(),
        'Exit': exit,
    }

    print("Action Menu")
    print("")
    for point, action in MENU_ACTS.items():
        print(f"\n\t{point} : {action}")