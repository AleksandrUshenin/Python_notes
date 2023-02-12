import Read_command

class UserInterface:

    def Print_menu(self):
        print(" Выбирите из списка команды:")
        print(" 1 - Добавить\n 2 - Вывести на экран список заметок\
            \n 3 - Вывести заметку с id\
            \n 4 - Удалить\n 5 - Редоктировать\n 6 - Загрузить\n 7 - Сохранить\n 0 - Выход")

    def Print_Notes(self, list_notes):
        print('\n\t\t Список заметок: \n')
        print('===================================================================================')
        for note in list_notes:
            print('\tid: {}'.format(note.id))
        
        Read_command.Read_line('')