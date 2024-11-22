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
            print('Книга не найдена, пожалуйста проверьте вводимые данные')

    def _save(self):
        with open('books.json', 'w') as add:
            json.dump(self.all_json, add)

    def _search_book(self, data_serch):
        if data_serch.isdigit():
            return data_serch
        else:
            for id_book in self.all_json:
                info_book = self.all_json[id_book]
                for i_f in info_book:
                    if info_book[i_f] == data_serch:
                        return id_book
        print('Книга не найдена, пожалуста проверьте данные на коректность')
        return None
        
    def addbook(self):
        title = input('Введите название книги: ')
        aythor = input('Введите имя и фамилию автора: ')
        year = input('Введите дату издания: ')
        self.all_json[3] = {'title':title, 'aythor':aythor, 'year':year, 'statys':STATUS_CHOISES['1']}
        self._save()
        print('Операция прошла успешно!')

    def cheng_status_book(self):
        data_for_chages_book = input('Введите id, название, автора, или дату издания книги: ')
        if data_for_chages_book.isdigit():
            id = self._search_book(data_for_chages_book)
            self._chenges(id)
        else:
            id = self._search_book(data_for_chages_book)
            self._chenges(id)
        print('Операция прошла успешно!')

    def delete_book(self):
        data_for_delete_book = input('Введите id, название, автора, или дату издания книги: ')
        id = self._search_book(data_for_delete_book)
        del self.all_json[id]
        self._save()

    def show_all_books(self):
        print('-----------')
        for i in self.all_json:
            print('id',i)
            for j in self.all_json[i]:
                print(j ,self.all_json[i][j])
            print('-----------')

        
if __name__ == '__main__':
    x = Book()
    x.show_all_books()