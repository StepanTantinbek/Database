def get_code():
    from data.const import CODE_LANG, UNKNOWN, CONSTPATH
    from data.lang_pack import LANGCODE


    if CODE_LANG == UNKNOWN:
        main_lang: str = ''
        print('Выберете язык:')
        for code, lan in LANGCODE.items():
            print(f'{code}) {lan}')
        while main_lang not in LANGCODE.keys():
            main_lang = input('> ')
        print(f'В системе будет использоваться {LANGCODE[main_lang]}')

        with open(CONSTPATH, "rt", encoding="utf-8") as pathchange:
            oldfile: list = pathchange.readlines()
        for index in range(len(oldfile)):
            if "CODE_LANG: int =" in oldfile[index]:
                oldfile[index] = f"CODE_LANG: int = {main_lang}\n"
                break
        with open(CONSTPATH, "wt", encoding="utf-8") as writing:
            print(*oldfile, sep="", end="", file=writing)
        return int(main_lang)
    else:
        return CODE_LANG
    