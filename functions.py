import os
import re
from typing import Any, Callable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/apache_logs.txt")   # вариант с разбора вместо 2 строк: FILE_NAME = 'data/apache_logs.txt'


def filter_query(param: str, data: None | list[str]) -> list[str]:
    """
    Функция фильтрации для первой обработки файла - по строчно или
    для массива, полученного другими способами сортировки - целиком.
    :param param: искомая строка.
    :param data: None или массив данных.
    :return: результат фильтрации.
    """
    filtering_result: list[str] = []

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


def map_query(param: str, data: None | list[str]) -> list[str]:
    """
    Функция сортировки по столбцам для первой обработки файла - по строчно или
    для массива, полученного другими способами сортировки - целиком.
    :param param: целое число в строчном представлении.
    :param data: None или массив данных.
    :return: результат сортировки.
    """
    maping_result: list[str] = []
    col_number: int = int(param)

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


def unique_query(data: list[str], *args: Any, **kwargs: Any) -> list[str]:
    """
    Функция выбора уникальных элементов из отфильтрованного массива.
    :param data: массив данных.
    :param args: любая строка.
    :param kwargs: любая строка.
    :return: результат выборки.
    """
    return list(set(data))


def sort_query(param: str, data: list[str]) -> list[str]:
    """
    Функция сортировки по возростанию (убыванию).
    :param param: 'asc' или любая днугая строка.
    :param data: массив данных.
    :return: результат выборки.
    """
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: list[str]) -> list[str]:
    """
    Функция получения среза для первой обработки файла - по строчно или
    из массива, полученного другими способами сортировки - целиком.
    :param param: целое число в строчном представлении.
    :param data: None или массив данных.
    :return: результат выборки.
    """
    limit: int = int(param)
    limiting_result: list[str] = []

    if data is None:
        with open(DATA_DIR) as file:
            for i in range(limit):
                line = next(file).strip()
                limiting_result.append(line)
    else:
        limiting_result = data[:limit]

    return limiting_result


def regex_query(param: str, data: list[str]) -> list[str]:
    """
    Функция фильтрации по регулярному выражению для первой обработки файла - по строчно или
    для массива, полученного другими способами сортировки - целиком.
    :param param: регулярное выражение.
    :param data: None или массив данных.
    :return: результат фильтрации.
    """
    filtering_result: list[str] = []
    pattern: re.Pattern[str] = re.compile(param)

    if data is None:
        with open(DATA_DIR) as file:
            while True:
                try:
                    prepared_data: str = next(file).strip()
                    if re.findall(pattern, prepared_data):
                        filtering_result.append(prepared_data)
                except StopIteration:
                    break
    else:
        filtering_result = list(filter(lambda x: re.search(pattern, x), data))

    return filtering_result


CMD_TO_FUNCTIONS: dict[str, Callable] = {
    'filter': filter_query,
    'sort': sort_query,
    'map': map_query,
    'unique': unique_query,
    'limit': limit_query,
    'regex': regex_query
}


def build_query(cmd: str, param: str, data: None | list[str]) -> list[str]:
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