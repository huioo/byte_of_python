import os
import pickle


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    @classmethod
    def is_same_type(cls, obj):
        return isinstance(obj, cls)


class Book:
    
    def __init__(self, size=20, number=100):
        self._page_size = size      # 每页大小
        self._page_number = number   # 页数

        self._data_file_path = 'address.data'
        # self._records = [None] * size * number
        self._records = self._load_local_data()

    def _load_local_data(self):
        """
        :return: @type dictionary
        """
        records = {}
        if os.path.exists(self._data_file_path):
            with open(self._data_file_path, 'rb') as f:
                records = pickle.load(f)
        return records

    def retrieve(self, rid):
        return self._records[rid]

    def write_one(self, record):
        self._records[record.rid] = record

    def save_to_local(self):
        with open(self._data_file_path, 'wb') as f:
            pickle.dump(self._records, f)


class AddressBook(Book):
    def retrieve(self, name):
        if name in self._records:
            return self._records[name]
    
    def add(self, record):
        if Person.is_same_type(record):
            self._records[record.name] = record

    def delete(self, record):
        if Person.is_same_type(record):
            del self._records[record.name]
            return True
        return False
    
    def all(self):
        return self._records


class Manager:
    def __init__(self, book):
        self._book = book
    
    def retrieve(self):
        name = input('\nEnter the name you want to query:')
        result = self._book.retrieve(name)
        if result:
            print(result.name, result.address, sep=', ')
        else:
            print('not found.')

    def add(self):
        name = input('\nEnter the name you want to add:')
        address = input('Enter the address you want to add:')
        person = Person(name, address)
        self._book.add(person)
        print('Successfully add one item.')

    def modify(self):
        name = input('\nEnter the name you want to modify:')
        result = self._book.retrieve(name)
        if not result:
            print('not found')
            return
        
        print(result.name, result.address, sep=', ')
        address = input('Enter the address you want to modify:')
        result.address = address
        print('Successfully modify.')

    def delete(self):
        name = input('\nEnter the name you want to delete:')
        result = self._book.retrieve(name)
        if not result:
            print('not found.')
            return

        if self._book.delete(result):
            print('Successfully delete.')
        else:
            print('Fail to delete.')

    def browse(self):
        if not self._book.all():
            print('There is no record')
        else:
            for name, person in self._book.all().items():
                print(name, person.address, sep=', ')
    

BOOK = AddressBook()
MANAGER = Manager(BOOK)
OPERATIONS = {
    'a': ('浏览', MANAGER.browse),
    'b': ('添加', MANAGER.add),
    'c': ('修改', MANAGER.modify),
    'd': ('删除', MANAGER.delete),
    'e': ('搜索', MANAGER.retrieve),
    'exit': ('退出', ''),
}


def main():
    print('*'*10, '地址簿', '*'*10)
    prompt = ' '.join([')'.join([k, v[0]]) for k, v in OPERATIONS.items()])
    while True:
        print(prompt)
        index = input('Enter the command you want to execute:\n').lower()
        if index not in OPERATIONS:
            print('type correct command.')
            continue
        if index == 'exit':
            break
        # 选择操作
        OPERATIONS[index][1]()
    
    # 退出之前保存
    BOOK.save_to_local()


if __name__ == '__main__':
    main()


