class Note:
    id : int = None
    data_note : str = None
    
    def __init__(self, id, note):
        self.id = id
        self.data_note = note

    def Add(self, id,  note):
        if note != None:  
            self.data_note = note
            self.id = id
