def get_code():
    from data.const import CODE_LANG, UNKNOWN, CONSTPATH
    from data.lang_pack import LANGCODE
    from localise_func.translator import get_localized_print
    if CODE_LANG == UNKNOWN:
        main_lang: str = ''
        print('Choose a language:')
        for code, lan in LANGCODE.items():
            print(f'{code}) {lan}')
        while main_lang not in LANGCODE.keys():
            main_lang = input('> ')
        localized_print = get_localized_print(code = int(main_lang))
        localized_print('The system will use', end = ' ') 
        print(LANGCODE[main_lang].lower())
        with open(CONSTPATH, "rt", encoding="utf-8") as pathchange:
            oldfile: list = pathchange.readlines()
        for index in range(len(oldfile)):
            if "CODE_LANG: int =" in oldfile[index]:
                oldfile[index] = f"CODE_LANG: int = {main_lang}\n"
                break
        with open(CONSTPATH, "wt", encoding="utf-8") as writing:
            print(*oldfile, sep="", end="", file=writing)
        localized_print('restart the application to continue')
        exit()
    else:
        return CODE_LANG
    