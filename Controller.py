import Read_command
from Notes import Notes

class Controller:
    _View = None
    _Message = None
    _Notes = Notes()

    def __init__(self, view):
        self._View = view

    def Add(self):
        header = Read_command.Read_line('Введите заголовок: ')
        self._Message = Read_command.Read_line('Введите заметку: ')
        self._Notes.Add_Note(header, self._Message)

    def Print_List_Notes(self):
        result = self._Notes.Get_unsorted()
        self._View.Print_List_Notes(result)
    
    def Print_Note(self):
        id = None
        try:
            id = int(Read_command.Read_line('Введите id: '))
        except:
            return
        result = self._Notes.Get_by_id(id)
        self._View.Print_Note(result)
    
    def Delete_Node(self):
        id = None
        try:
            id = int(Read_command.Read_line('Введите id: '))
        except:
            return
        self._Notes.Delete(id)

    def Edit_Node(self):
        id = None
        try:
            id = int(Read_command.Read_line('Введите id: '))
        except:
            return
        header = Read_command.Read_line('Введите заголовок: ')
        self._Message = Read_command.Read_line('Введите Заметку: ')
        self._Notes.Edit(id, header, self._Message)
