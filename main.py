import functions

while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. удаление, 5. изменение')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.delit_data()
    elif mode == 5:
        functions.change_data()
    else:
        break

# with open('book.txt', 'w', encoding='utf-8') as f:
#     f.write('ФИО | номер телефона')
#
# with open('book.txt', 'a', encoding='utf-8') as f:
#     f.write('\nФИО1 | номер телефона1')
#
# with open('book.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# FIO | 20343
# FIO1 | 394032
# FIO3 | 3945543