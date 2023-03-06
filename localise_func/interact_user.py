def get_code():
    from os.path import join, split as filesplit
    from const import CODE_LANG, UNKNOWN, CONST_FILE_NAME
    from lang_logs import CODE_RUS, CODE_ENG, CODE_IT
    from main import FILEPATH


    if CODE_LANG == UNKNOWN:
        lang: dict = {
            CODE_RUS: 'Русский язык',
            CODE_ENG: 'Английский язык',
            CODE_IT: 'Итальянсий язык',
        }


        main_lang: str = ''
        print('Выберете язык:')
        for code, lan in lang.items():
            print(f'{code}) {lan}')
        while main_lang not in lang.keys():
            main_lang = input('> ')
        print(f'В системе будет использоваться {lang[main_lang]}')

        DIRNAME, _ = filesplit(FILEPATH)
        CONST_PATH: str = join(DIRNAME, CONST_FILE_NAME)
        with open(CONST_PATH, "rt", encoding="utf-8") as pathchange:
            oldfile: list = pathchange.readlines()
        for index in range(len(oldfile)):
            if "CODE_LANG: int =" in oldfile[index]:
                oldfile[index] = f"CODE_LANG: int = {main_lang}\n"
                break
        with open(CONST_PATH, "wt", encoding="utf-8") as writing:
            print(*oldfile, sep="", end="", file=writing)
    else:
        return CODE_LANG