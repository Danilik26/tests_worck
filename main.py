import json

STATUS_CHOISES = {
    '1':'В наличии',
    '2':'Выданна',
}

class Book:
    def __init__(self):
        self.all_json = self._get_all_json()

    def _get_all_json(self):
        with open('books.json','r') as a:
            return json.load(a)
        
    def _chenges(self, data_for_chages_book):
        try:
            book = self.all_json[data_for_chages_book]
            type_status = input('Для изменения статуса на \'в наличии\' введите 1 \n'
                                'для изменения статуса на \'выданна\' ddtlbnt 2\n'
                                'Введите операцию: ')
            if type_status == '1':
                book['statys'] = STATUS_CHOISES[type_status]
            elif type_status == '2':
                book['statys'] = STATUS_CHOISES[type_status]
            self._save()
        except KeyError:
            print('Книга не найдена,  пожалуйста проверьте вводимые данные')

    def _save(self):
        print(self.all_json)
        with open('books.json', 'w') as add:
            json.dump(self.all_json, add)
        
    def addbook(self):
        title = input('Введите название книги: ')
        aythor = input('Введите имя и фамилию автора: ')
        year = input('Введите дату издания: ')
        self.all_json[3] = {'title':title, 'aythor':aythor, 'year':year, 'statys':'выдана'}
        self._save()
            

    def cheng_status_book(self):
        data_for_chages_book = input('Введите id, название, автора, или дату издания книги: ')
        if data_for_chages_book.isdigit():
            self._chenges(data_for_chages_book)
        else:
            for id_book in self.all_json:
                info_book = self.all_json[id_book]
                for i_f in info_book:
                    if info_book[i_f] == data_for_chages_book:
                        self._chenges(id_book)
        # with open('books.json', 'w') as s:
        #     read_json['dcs'] = 1
        #     print(json.dump(read_json, s))
if __name__ == '__main__':
    x = Book()
    print(x.all_json)