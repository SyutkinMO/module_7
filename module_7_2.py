#-------------------Позиционирование в файле-------------------

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name
# - название файла для записи, strings - список строк для записи.
# Функция должна: Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка.

def custom_write(file_name, strings):

    base = {}

    file = open(f'{file_name}.txt', 'w+', encoding='utf-8')
    counter = 1
    bite_ = 0

    for i in strings:
        file.write(f'{i}\n')
        base[(counter, bite_)] = i
        counter += 1
        bite_ = file.tell()

    file.close()

    return base

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name
# - название файла для записи, strings - список строк для записи.
# Функция должна: Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка.

