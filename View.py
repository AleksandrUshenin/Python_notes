import Read_command

class UserInterface:

    def Print_menu(self):
        print(" Выбирите из списка команды:")
        print(" 1 - Добавить\n 2 - Вывести на экран список заметок\
            \n 3 - Вывести заметку с id\
            \n 4 - Удалить\n 5 - Редоктировать\n 6 - Загрузить\n 7 - Сохранить\n 0 - Выход")

    def Print_List_Notes(self, list_notes):
        print('\n\t\t Список заметок: \n')
        print('===================================================================================')
        for note in list_notes:
            print('\tid: {}   header: {}   date time: {}'.format(note.id, note.header, note.date))
        
        Read_command.Read_line('')

    def Print_Note(self, note):
        if note == None:
            return
        print('\n\tЗаметка с id: {}'.format(note.id))
        print('\n header: {}'.format(note.header))
        print('\n body: \n{}'.format(note.body))
        Read_command.Read_line('')