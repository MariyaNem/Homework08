from array import *

def show_data() -> None:
    '''Выводит инфу из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет инфу в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')

def find_data() -> None:
    '''Осуществляет поиск по справочникам'''
    find = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, find))

def search(book: str, info: str) -> str:
    '''Находит в строке записи по опр. критерию поиска '''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def delit_data() -> None:
    '''Удаление данных из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    delited = False
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in enumerate(tel_book):
            if data not in line:
                f.write(line)
            else:
                deleted = True

def change_data() -> None:
    '''Изменение данных в справочнике'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
        new_list = list(tel_book)
        incorr_data = input('Введите данные для изменения ')
    with open('book.txt', 'w', encoding='utf-8') as f:
        if incorr_data in new_list:
            corr_data = input('Введите корректные данные ')
            new_list[new_list.index(incorr_data)] = corr_data
            print('Запись изменена')
        f.write(' '.join(map(str, new_list)))