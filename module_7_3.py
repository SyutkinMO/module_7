# ------------Оператор "with".------------


class WordsFinder():
    """
    Объект этого класса должен принимать при создании неограниченного количество названий файлов
    и записывать их в атрибут file_names в виде списка или кортежа.
    """

    file_names = []  # список с названиями всех файлов

    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        """
        get_all_words - подготовительный метод, который возвращает словарь следующего вида:
        {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        Где:
        'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
        ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
        """
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                string_ = ''            # text = file.read().lower() - как вариант
                for j in file:
                    string_ += j.lower()
                import re
                string_ = re.sub(r'[.,=!?;:-]', '', string_)  # удаление знаков препинания
                string_ = re.sub(r'[\n]', ' ', string_)  # замена переносов на пробел
                all_words[i] = string_.split(' ')  # разбаить строку по пробелам
        return all_words

    def find(self, word):
        """
        метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        """

        dict_find = {}
        low_word = word.lower()
        for name, words in self.get_all_words().items():
            if low_word in words:
                dict_find[name] = words.index(low_word) + 1
        return dict_find

    def count(self, word):

        """
        count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла.
        """

        dict_count = {}
        low_word = word.lower()
        for name, words in self.get_all_words().items():
            if low_word in words:
                dict_count[name] = words.count(low_word)
        return dict_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TExt'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
