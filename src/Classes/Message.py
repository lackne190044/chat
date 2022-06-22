from datetime import datetime

class Message:
    """Class represanting a message."""
    def __init__(self, username, text, date = datetime.now()):
        """Initialize the message."""
        self._username = username 
        if type(self._username) != str:
            self._username = self._username._username
        self._text = text
        self._date = date

    @property
    def json(self):
        """Convert the data of the message in to a json string."""
        return { 'date': str(self._date), 'user': self._username, 'text': self._text}
