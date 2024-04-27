import csv
from config import ROOT
import os


def get_file_paths(dir_path):
    """
    Возвращает пути к файлам из указанного каталога  dir_path
    """
    return [os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path)]


def get_file_name(path):
    """
    Получает имя файла из пути к файлу
    """
    return os.path.basename(path).split('/')[-1]


def read_csv_data(file_path):
    """
    Читает данные из csv в список
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        return list(reader)


def get_all_csv_data():
    """
    Возвращает список списков:
    [[имя таблицы БД, данные для вставки],
    [имя таблицы БД, данные для вставки],
    ...]
    """
    all_csv_data = []
    dir_path = os.path.join(ROOT, "homework-1", "north_data")
    for file_path in get_file_paths(dir_path):
        table_name = get_file_name(file_path).split('_')[0]
        items_data = read_csv_data(file_path)
        all_csv_data.append([table_name, items_data])

    return all_csv_data


def parse_if_num_like_int(value):
    """
    Преобразует float k int, если при этом не произойдет округление.
    """
    if not isinstance(value, float):
        return value

    if value != int(value):
        return value
    return int(value)
