from .base import perfect_dt


POS_ANW: tuple = ("yes", "sure", "ye", "yeah")
NEG_ANW: tuple = ("no", "nah")


def notification(flag: bool, pos: str='', neg: str ='') -> bool:
    '''Bool function that prints negative or positive comment.'''
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
    '''Asks user a question and returns bool depending on answer.'''
    answ: str = ""
    if notification:
        print(notification)
    while answ not in posanswer + neganswer:
        answ = perfect_dt(input(question))
        if answ in posanswer:
            return True
        elif answ in neganswer:
            return False
        else:
            print("We did not understand you")
            print(
                "Please use answers presented: POSITIVES: "
                f"({', '.join(posanswer)}) or NEGATIVES: "
                f"({', '.join(neganswer)})"
            )