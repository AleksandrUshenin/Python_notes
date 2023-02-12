from Note import Note
from datetime import datetime

class Notes:
    _Next_id = 0
    _Notes = []

    def Add_Note(self, header, notes):
        time = datetime.now()
        if notes != None:
            self._Notes.append(Note(self._Next_id, header, notes, time))
            self._Next_id += 1

    def Get_by_id(self, id):
        result = None
        for item in self._Notes:
            if item.id == id:
                result = item
        return result 

    def Delete(self, id):
        flag = False
        for item in self._Notes:
            if item.id == id:
                self._Notes.remove(item)

    def Edit(self, id, header, node):
        if self.Exist(id):
            time = datetime.now()
            item : Note = None
            item = self.Get_by_id(id)
            item.Edit(header, node, time)

    def Exist(self, id):
        if self.Get_by_id(id) != None:
            return True
        return False

    def Imort(self, list_node):
        self._Notes = list_node
        #for item in list_node:
        #    self._Notes.append(Note(item.id, item.header, item.notes, datetime(item.time)))
    
        
    #def Get_sorted(self):
        #return sorted([item for item in self._Notes], key = lambda row:(row.surname, row.name, row.patronymic))

    def Get_unsorted(self):
        return self._Notes
