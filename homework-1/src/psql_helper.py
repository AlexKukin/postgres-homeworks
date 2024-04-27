from utils import parse_if_num_like_int
import psycopg2


def fill_db_table(cur, table_name, items_data):
    """
    Заполняет таблицу table_name данными items_data
    """
    for item_data in items_data:
        item_data = list(map(parse_if_num_like_int, item_data))
        formats = ['%s'] * len(item_data)
        cur.execute(f'INSERT INTO {table_name} VALUES ({", ".join(formats)})', tuple(item_data))


def fill_db_tables(insert_data_list):
    """
    Заполняет таблицы БД north из данных insert_data_dict
    """
    conn_params = {
        "host": "localhost",
        "database": "north",
        "user": "postgres",
        "password": "12345"
    }
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            for table_name, items_data in insert_data_list:
                no_header_data = items_data[1:]
                fill_db_table(cur, table_name, no_header_data)
                # print_table(cur, table_name)
    conn.close()


def print_db_table(cur, table_name):
    """
    Выводит содержимое таблицы table_name в консоль
    """
    cur.execute(f'SELECT * FROM  {table_name}')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print('------------')
