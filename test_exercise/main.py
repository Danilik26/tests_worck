import json
from json.decoder import JSONDecodeError
from typing import Dict

JSON_FIEL_NAME = 'books.json'

STATUS_CHOISES = {
    '1':'В наличии',
    '2':'Выданна',
}

class Book:
    def __init__(self):
        self.all_json: Dict = self._get_all_json() # all data from json file

    """
    function get all json data from said json fiel
    """    

    def _get_all_json(self) -> Dict :
        with open(JSON_FIEL_NAME,'r') as a:
            try:
                return json.load(a)
            except JSONDecodeError:
                return {}
            
    """
    function return next id for new book
    """

    def _next_id(self) -> int:
        try:
            return int(list(self.all_json.keys())[-1]) + 1
        except:
            return 1
        
    """
    function get code for chenge status 
    make chenge status for specified book
    save change 
    """
        
    def _chenges_status(self, data_for_chages_book: str) -> bool:
        try:
            book: Dict = self.all_json[data_for_chages_book]
            type_status: str = input('Для изменения статуса на \'в наличии\' введите 1 \n'
                                'для изменения статуса на \'выданна\' 2\n'
                                'Введите операцию: ')
            if type_status == '1':
                book['statys'] = STATUS_CHOISES[type_status]
            elif type_status == '2':
                book['statys'] = STATUS_CHOISES[type_status]
            self._save()
            return True
        except KeyError:
            print('Книга не найдена, пожалуйста проверьте вводимые данные\n')
            return False

    """
    function save all chenges in books and save new add book 
    """

    def _save(self):
        with open(JSON_FIEL_NAME, 'w') as add:
            json.dump(self.all_json, add)

    """
    function sherch id book from specified data for sherch 
    return id found book
    """

    def _search_id_book(self, data_serch: str) -> bool:
        if data_serch.isdigit():
            if data_serch not in self.all_json.keys():
                print('Книга не найдена, пожалуста проверьте данные на коректность\n')
                return False
            return data_serch
        else:
            for id_book in self.all_json:
                info_book: bool = self.all_json[id_book]
                for i_f in info_book:
                    if info_book[i_f] == data_serch:
                        return id_book
        print('Книга не найдена, пожалуста проверьте данные на коректность\n')
        return None
    
    def _cheack_year(self, year: str) -> bool:
        if year.isdigit():
            return True
        else:
            return False
        
    def addbook(self):
        title: str = input('Введите название книги: ')
        print('------')
        aythor: str = input('Введите имя и фамилию автора: ')
        print('------')
        year: str = input('Введите год издания: ')
        print('\n')
        if self._cheack_year(year):
            self.all_json[self._next_id()] = {'title':title, 'aythor':aythor, 'year':year, 'statys':STATUS_CHOISES['1']}
            self._save()
            print('Операция прошла успешно!\n')
        else:
            print('Невернно введён год издания, попробуйте ещё раз\n')
            self.addbook()
        input('Для продолжения действия нажмите любую кнопку')

    def cheng_status_book(self):
        data_for_chages_book: str = input('Введите id, название, автора, или дату издания книги: ')
        print('\n')
        if data_for_chages_book.isdigit():
            id: bool = self._search_id_book(data_for_chages_book)
            if id:
                cheng: bool = self._chenges_status(id)
                if cheng:
                    print('Операция прошла успешно! \n')
            else:
                self.cheng_status_book()
        else:
            id: bool = self._search_id_book(data_for_chages_book)
            if id:
                cheng: bool = self._chenges_status(id)
                if cheng:
                    print('Операция прошла успешно!')
            else:
                self.cheng_status_book()
        input('Для продолжения действия нажмите любую кнопку')
        

    def delete_book(self):
        data_for_delete_book: str = input('Введите id, название, автора, или дату издания книги: ')
        print('\n')
        id: bool = self._search_id_book(data_for_delete_book)
        if id:
            del self.all_json[id]
            self._save()
            print('Операция прошла успешно!')
        else:
            self.delete_book()
        input('Для продолжения действия нажмите любую кнопку')

    def show_all_books(self):
        print('-----------')
        for i in self.all_json:
            print('id', ':',i)
            for j in self.all_json[i]:
                print(j, ':' ,self.all_json[i][j])
            print('-----------')
        input('Для продолжения действия нажмите любую кнопку')

    def swow_one_book(self):
        print('Все авторы')
        for i in self.all_json:
            for x in self.all_json[i]:
                if x == 'aythor':
                    print(self.all_json[i][x])
        dataserh: str = input('Введите id, название, автора, или дату издания книги: ')
        print('\n')
        id_book: bool = self._search_id_book(dataserh)
        if id_book:
            for i in self.all_json[id_book]:
                print(i, ':', self.all_json[id_book][i])
        input('Для продолжения действия нажмите любую кнопку')
        
if __name__ == '__main__':
    while True:
        book = Book()
        action = input('Для просмотра всех книг введите 1 \n'
                       '\n'
                       'для просмо конкретной книги введите 2 \n'
                       '\n'
                       'для удаления книги введите 3 \n'
                       '\n'
                       'для втавки новой книги введите 4 \n'
                       '\n'
                       'для зменения статуса книги введите 5 \n'
                       '\n'
                       'для окончания работы введите 6 \n'
                       '\n'
                       'поле ввода: ')
        if action == '1':
            book.show_all_books()
        elif action == '2':
            book.swow_one_book()
        elif action == '3':
            book.delete_book()
        elif action == '4':
            book.addbook()
        elif action == '5':
            book.cheng_status_book()
        elif action == '6':
            break
        else:
            print('Код операции не верен, попробуйте ещё раз \n')