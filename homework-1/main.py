"""Скрипт для заполнения данными таблиц в БД Postgres."""
from src.psql_helper import fill_db_tables
from src.utils import get_all_csv_data


def main():
    """
    Точка входа. Программа заполнения таблиц БД north из csv файлов
    """
    all_csv_data = get_all_csv_data()
    fill_db_tables(all_csv_data)


if __name__ == '__main__':
    main()


