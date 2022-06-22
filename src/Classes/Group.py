from Classes.User import User

class Group:
    """Class representing a group."""
    def __init__(self, name: str, owner: User):
        """Initializing the group."""
        self._name = name
        self._owner = owner._username
        self._usernames = []
        self._admins = []
        self._messages = []

    def addMessage(self, message):
        """Adds a message to the group."""
        self._messages.append(message.json)

    def removeMessage(self, message):
        """Removes a message from the group"""
        for i in self._messages:
            if i == message:
                del i

    def addUser(self, username):
        """Add a user to the group"""
        if type(username) != str:
            username = username._username
        self._usernames.append(username)

    def removeUser(self, username):
        """Remove a user from the group"""
        for i in self._usernames:
            if i == username:
                del i

    def addAdmin(self, username):
        """Promote a user to admin"""
        for i in self._user:
            if i == username:
                self._admins.append(i)

    def removeAdmin(self, username):
        """Demote a admin to a user"""
        for i in self._admins:
            if i == username:
                del i

    @property
    def json(self):
        """Create a json string"""
        data = {
            'name': self._name,
            'owner': self._owner,
            'usernames': self._usernames,
            'admins': self._admins,
            'messages': self._messages
        }
        return data
