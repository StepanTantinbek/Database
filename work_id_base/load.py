def relation_load(
        id: __import__("typing").Union[str, int],
        separator: str = __import__("data").const.SEPTAB_SPACES
    ) -> tuple[tuple[int], tuple[int]]:
    '''Reads database and returns tuple of friends and chats of the user.'''
    def read_relation(string: str) -> tuple[tuple[ int], tuple[int]]:
        '''Returns friends ids and chat ids.'''
        def split_tuple(element: str) -> tuple[int]:
            '''Makes tuple for friends and chat ids.'''
            from data.const import SPACE
            step1 = element.strip()
            print(step1)
            if not step1:
                return tuple()
            elif SPACE not in step1:
                return int(step1),
            else:
                return tuple(map(int, step1.split(SPACE)))
        line_demo: list[str] = line.split(separator)[1:]
        friends_id, chat_id = tuple(map(split_tuple, line_demo))
        return friends_id, chat_id
    from data.const import RELATIONPATH, SEPTAB
    from os.path import exists
    if exists(RELATIONPATH):
        with open(RELATIONPATH, "rt", encoding="utf-8") as readfile:
            fields: tuple[str] = tuple(readfile.readline().split(separator))
            data: list[str] = readfile.readlines()
            for line in data:
                if line.startswith(f"{str(id)} "):
                    datas: tuple[str] = read_relation(line)
                    return datas
            print("ID doesn't exist in database.")
    return (tuple(), tuple())