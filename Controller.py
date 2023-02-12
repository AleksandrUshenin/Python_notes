import Read_command
from Notes import Notes

class Controller:
    _View = None
    _Message = None
    _Notes = Notes()

    def __init__(self, view):
        self._View = view

    def Add(self):
        self._Message = Read_command.Read_line('Введите заметку: ')
        self._Notes.Add_Note(self._Message)

    def Print_Notes(self):
        res = self._Notes.Get_unsorted()
        self._View.Print_Notes(res)