class User():
    id: int
    id_list_friend: tuple[int]
    id_list_chat: tuple[int]
    name: str
    surname: str
    nickname: str
    login: str
    age: str

    is_change: bool

    def __init__(self, get_id: int, id_user: int, data: int):
        from work_id_base.user_work import lookup_user
        from work_id_base.load import relation_load

        self.id = id_user
        self.name = data["NAME"]
        self.age = int(data["AGE"])
        self.surname = data["SURNAME"]
        self.nickname = data["NICKNAME"]
        self.login = data["LOGIN"]
        self.is_change = False

        if lookup_user(self.id):
            self.id_list_friend, self.id_list_chat = relation_load
            self.id_list_friend = map(int, self.id_list_friend)
            self.id_list_chat = map(int, self.id_list_chat)
        else:
            self.id_list_friend = tuple()
            self.id_list_chat = tuple()

    def add_new_friends(self, id_friend: int) -> None:
        self.is_change = True
        self.id_list_friend = tuple(list(self.id_list_friend) + [id_friend])
        '''Make it add id to baza_relations.'''

    def add_new_chat(self, id_chat: int) -> None:
        self.is_change = True
        self.id_list_chat = tuple(list(self.id_list_chat) + [id_chat])
        '''Make it add id to baza_relations.'''

    def remove_friend(self, id_friend: int) -> None:
        if id_friend in self.id_list_friend:
            self.is_change = True
            list_friend = list(self.id_list_friend)
            list_friend.remove(id_friend)
            self.id_list_friend = tuple(list_friend)
        else:
            print(f"The person with id: {id_friend} is not your friend")
        '''Make it remove it from baza_relations.'''

    def remove_chat(self, id_chat: int) -> None:
        if id_chat in self.id_list_chat:
            self.is_change = True
            list_chat = list(self.id_list_chat)
            list_chat.remove(id_chat)
            self.id_list_chat = tuple(list_chat)
        else:
            print(f"The person with id: {id_chat} does not have chat with you")
        '''Make it remove it from baza_relations.'''

    def save(self) -> bool: