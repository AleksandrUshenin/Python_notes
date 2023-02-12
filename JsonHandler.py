import json
import os
import os.path

class JsonHandler:

    def Export(self, note_list):
        if not os.path.exists('data'):
            os.mkdir('data')
        data = []
        for item in note_list:
            data.append(JsonHandler.get_dict(item))
        file = open('data\\database.json', 'w')
        json.dump(data, file)
        file.close()

    def importin(self):
        book = []
        file_paths = 'data\\database.json'
        if not os.path.exists(file_paths):
            return []
        file = open(file_paths)
        data = json.load(file)
        for item in data:
            book.append(create_contact_by_dictionary(item))
        return book
    
    def get_dict(item):
        item = item
        dict = {'id': item.id,
                'header': item.header,
                'body': item.body,
                'date': str(item.date)
                }
        return dict