import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/apache_logs.txt")   # вариант с разбора вместо 2 строк: FILE_NAME = 'data/apache_logs.txt'


def filter_query(param, data):
    """
    Функция фильтрации для первой обработки файла - по строчно или
    для массива, полученного другими способами сортировки - целиком.
    :param param: искомая строка.
    :param data: None или массив данных.
    :return: результат фильтрации.
    """
    filtering_result = []

    if data is None:
        with open(DATA_DIR) as file:
            while True:
                try:
                    prepared_data = next(file).strip()
                    if param in prepared_data:
                        filtering_result.append(prepared_data)
                except StopIteration:
                    break
    else:
        filtering_result = list(filter(lambda x: param in x, data))

    return filtering_result


def map_query(param, data):
    """
    Функция сортировки для первой обработки файла - по строчно или
    для массива, полученного другими способами сортировки - целиком.
    :param param: целое число в строчном представлении.
    :param data: None или массив данных.
    :return: результат сортировки.
    """
    maping_result = []
    col_number = int(param)

    if data is None:
        with open(DATA_DIR) as file:
            while True:
                try:
                    prepared_data = next(file).strip()
                    maping_result.append(prepared_data.split(' ')[col_number])
                except StopIteration:
                    break
    else:
        maping_result = list(map(lambda x: x.split(' ')[col_number], data))

    return maping_result


def unique_query(data, *args, **kwargs):
    """
    Функция выбора уникальных элементов из отфильтрованного массива.
    :param data: массив данных.
    :param args: любая строка.
    :param kwargs: любая строка.
    :return: результат выборки.
    """
    return list(set(data))


def sort_query(param, data):
    """
    Функция сортировки по возростанию (убыванию).
    :param param: 'asc' или любая днугая строка.
    :param data: массив данных.
    :return: результат выборки.
    """
    reverse = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param, data):
    """
    Функция получения среза для первой обработки файла - по строчно или
    из массива, полученного другими способами сортировки - целиком.
    :param param: целое число в строчном представлении.
    :param data: None или массив данных.
    :return: результат выборки.
    """
    limit = int(param)
    limiting_result = []

    if data is None:
        with open(DATA_DIR) as file:
            for i in range(limit):
                line = next(file).strip()
                limiting_result.append(line)
    else:
        limiting_result = data[:limit]

    return limiting_result


CMD_TO_FUNCTIONS = {
    'filter': filter_query,
    'sort': sort_query,
    'map': map_query,
    'unique': unique_query,
    'limit': limit_query
}


def build_query(cmd, param, data):
    """
    Функция сопостовления по ключу и запуска нужной функции.
    :param cmd: ключевое слово из CMD_TO_FUNCTIONS.
    :param param: параметр для обработки нужной функции.
    :param data: данные для обработки нужной функцией.
    :return: результат работы нужной функции.
    """
    return CMD_TO_FUNCTIONS[cmd](param=param, data=data)



# Варианты с разбора:
# def filter_query(param, data):
#     return list(filter(lambda x: param in x, data))
#
#
# def map_query(param, data):
#     col_number = int(param)
#     return list(map(lambda x: x.split(' ')[col_number], data))
#
#
# def unique_query(data, *args, **kwargs):
#     return list(set(data))
#
#
# def sort_query(param, data):
#     reverse = False if param == 'asc' else True
#     return sorted(data, reverse=reverse)
#
#
# def limit_query(param, data):
#     limit = int(param)
#     return list(data)[:limit]