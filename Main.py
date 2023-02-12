from View import UserInterface
import Read_command
from Controller import Controller

class Program:
    _View = UserInterface()
    _Control = Controller(_View)

    def Run(self):
        Do = True

        while Do:
            self._View.Print_menu()
            Do = self.Do_Commands(Read_command.Read_line("-- "))
    
    def Do_Commands(self, id_command):
        if id_command == '0':
            return False
        elif id_command == '1':
            self._Control.Add()
        elif id_command == '2':
            self._Control.Print_List_Notes()
        elif id_command == '3':
            self._Control.Print_Note()
        elif id_command == '4':
            self._Control.Delete_Node()
        elif id_command == '5':
            self._Control.Edit_Node()   
            
        return True