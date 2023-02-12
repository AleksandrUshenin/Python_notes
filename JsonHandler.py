import json
import os
import os.path
from Note import Note
from datetime import datetime

class JsonHandler:

    def Export(self, note_list):
        if not os.path.exists('data'):
            os.mkdir('data')
        data = []
        for item in note_list:
            data.append(JsonHandler.Get_dict(item))
        file = open('data\\database.json', 'w')
        json.dump(data, file)
        file.close()

    def Import(self):
        list_note = []
        file_paths = 'data\\database.json'
        if not os.path.exists(file_paths):
            return []
        file = open(file_paths)
        data = json.load(file)
        for item in data:
            list_note.append(self.Create_contact_by_dictionary(item))
        return list_note
    
    def Get_dict(item):
        item = item
        dict = {'id': item.id,
                'header': item.header,
                'body': item.body,
                'date': str(item.date)
                }
        return dict

    def Create_contact_by_dictionary(self, item):
        cont = Note(int(item['id']), item['header'], item['body'], (item['date']))
        return cont