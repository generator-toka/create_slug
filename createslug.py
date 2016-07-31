"""(ru)Модуль для создания слагов с русского языка на английскую
    транслитерацию.
    Включает в себя функцию create_slug и класс CreateSlug,
    а так же словарь с транслитерацией.
    (en)Module to create slug from Russian into English transliteration.
    Includes function create_slug and class CreateSlug,
    as well as a dictionary with transliteration."""


import string
import re


replace_russian = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
                   "е": "e", "ё": "yo", "ж": "zh", "з": "z",
                   "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
                   "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
                   "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch",
                   "ш": "sh", "щ": "sch", "ь": "", "ы": "i", "ъ": "",
                   "э": "e", "ю": "yu", "я": "ya", ",": "-", "-": "-",
                   ".": "-", " ": "-"}


def create_slug(phrase):
    """(ru)Функция для создания слагов с русского языка
       на английскую транслитерацию.
       (en)The function to create a slug from Russian
       the English transliteration .
       """
    phrase.lower()
    temp_list = []
    for letter in phrase:
        if letter in replace_russian.keys():
            temp_list.append(replace_russian[letter])

        elif letter in string.ascii_letters:
            temp_list.append(letter)

        else:
            temp_list.append('')

    temp_slug = ''.join(temp_list)[:300]

    result = re.sub(r'-+', '-', temp_slug)

    if result.startswith('-'):
        result = result[1:]
    if result.endswith('-'):
        result = result[:-1]
    return result


class CreateSlug:

    """(ru)Класс для создания слагов с русского языка
       на английскую транслитерацию.
       (en)Class to create a slug from Russian
       the English transliteration .
    """

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def create_slug(self):
        temp_list = []
        for letter in self.phrase:
            if letter in replace_russian.keys():
                temp_list.append(replace_russian[letter])

            elif letter in string.ascii_letters:
                temp_list.append(letter)

            else:
                temp_list.append('')

        temp_slug = ''.join(temp_list)[:300]

        result = re.sub(r'-+', '-', temp_slug)

        if result.startswith('-'):
            result = result[1:]
        if result.endswith('-'):
            result = result[:-1]
        return result

    def __str__(self):
        return 'your slug is \'{}\''.format(self.create_slug())


if __name__ == '__main__':
    import time

    start = time.clock()
    x_func = create_slug('--------здесь []  будет ... много пробелов------  ')
    print(x_func, '\'this is function\'')
    finish = time.clock()

    print(finish - start, 'sec')

    b_class = CreateSlug('//\'-----здесь []  будет ... много пробелов-///-  ')
    print(b_class.create_slug(), '\'this is class method\'')
    print(b_class.phrase, '\'this is phrase\'')
    print(b_class)
