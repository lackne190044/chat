from Classes.User import User

class Group:
    def __init__(self, name: str, owner: User):
        self._name = name
        self._owner = owner._username
        self._usernames = []
        self._admins = []
        self._messages = []

    def addMessage(self, message):
        self._messages.append(message.json)

    def removeMessage(self, message):
        for i in self._messages:
            if i == message:
                del i

    def addUser(self, user):
        self._usernames.append(user._username)

    def removeUser(self, username):
        for i in self._usernames:
            if i == username:
                del i

    def addAdmin(self, username):
        for i in self._user:
            if i == username:
                self._admins.append(i)

    def removeAdmin(self, username):
        for i in self._admins:
            if i == username:
                del i

    @property
    def json(self):
        data = {
            'name': self._name,
            'owner': self._owner,
            'usernames': self._usernames,
            'admins': self._admins,
            'messages': self._messages
        }
        return data
