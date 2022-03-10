from datetime import datetime

class Message:
    def __init__(self, username, text, date = datetime.now()):
        self._username = username 
        self._text = text
        self._date = date

    @property
    def json(self):
        return { 'date': str(self._date), 'user': self._username, 'text': self._text}
