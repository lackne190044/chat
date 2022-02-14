from datetime import datetime

class Message:
    def __init__(self, user, text, date = datetime.now()):
        self._user = user 
        self._text = text
        self._date = date
