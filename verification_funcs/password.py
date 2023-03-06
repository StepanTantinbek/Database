

'''includes functions to create a strong password.'''


from interact_funcs.base import perfect_dt
from interact_funcs.user import notification
from string import ascii_lowercase
from verification_funcs.auxiliary import lencheck
from getpass import getpass as hiddeninput
from const import MAX_RPT_CHR


def checkpssw() -> str:
    '''checks password.'''


    def repeat_check(passw: str) -> bool:
        '''checks if any symbol is repeated to many times.'''
        if passw:
            perfect_data: str = perfect_dt(passw)
            cnt: int = 1
            for index, chr in enumerate(perfect_data[:-1]):
                if chr == perfect_data[index + 1]:
                    cnt += 1
                    if cnt == MAX_RPT_CHR:
                        print(
                            "Characters should not be repeated "
                            f"more than {MAX_RPT_CHR} times"
                        )
                        return False
                else:
                    cnt = 1
            return True
        else:
            print(
                "Characters should not be repeated "
                f"more than {MAX_RPT_CHR} times"
            )


    def charcheck(passw: str) -> bool:
        '''checks for types of chars need in password.'''
        perfect_data = perfect_dt(passw)
        letters: bool = False
        numbers: bool = False
        chars: bool = False
        for char in perfect_data:
            if char in ascii_lowercase:
                letters = True
            elif char.isdigit():
                numbers = True
            else:
                chars = True
        return notification(
            all(
                (letters, numbers, chars)
            ),
                neg="Use letters, number and special characeters"
        )


    def checkreg(passw: str) -> bool:
        '''checks is password uses upper and lower register.'''
        return notification(
            passw and not (passw.isupper() or passw.islower()),
            neg="You have to use both high a low register for letters"
        )


    def forblistcheck(passw: str) -> bool:
        '''checks if password has popular char combos.'''
        if passw:
            perfect_data = perfect_dt(passw)
            FORB_LIST: tuple = (
                "qwer",
                "pass",
                "abcde"
            )
            for word in FORB_LIST:
                if word in perfect_data:
                    print(f"Popular char combination: ({word})")
                    return False
            return True
        else:
            print("Password cannot have popular character combos")

     
    data: str = ""
    print("Rules for password creation:")
    while not all((
        checkreg(data),
        forblistcheck(data),
        charcheck(data),
        lencheck(data),
        repeat_check(data)
    )):
        print("\n\nType in new <PASSWORD>: ", end="")
        data = hiddeninput()
    print("\ngreat password\n\n")
    return data