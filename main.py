import json
class Book:
    def addbook(self):
        title = input('Введите название книги: ')
        Aythor = input('Введите имя и фамилию автора: ')
        year = input('Введите дату издания: ')
        json_data = main()
        with open('books.json', 'w'):
            pass

def main(author_name):
    with open('books.json','r') as a:
        return json.load(a)
def changes():
    book_for_changes = input('Введите имя и фамилию автора для изменения')
    read_json = main(author_name = book_for_changes)
    with open('books.json', 'w') as s:
        read_json['dcs'] = 1
        print(json.dump(read_json, s))

x = {
    'books':{
        1:{
            'title':'fvdsv',
            'Author':'cedds',
            'year':'vdscv',
            'statys':'cscedws'
        }
    }
}