from datetime import datetime

class Note:
    id : int = None
    header : str = None
    body : str = None
    date : datetime = None

    def __init__(self, id : int, header : str, note_body : str, time : datetime):
        self.id = id
        self.header = header
        self.body = note_body
        self.date = time

    def Add(self, id,  note_body):
        if note_body != None:  
            self.body = note_body
            self.id = id
