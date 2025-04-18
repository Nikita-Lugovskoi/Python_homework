import os
import json

from dotenv import load_dotenv
import pyodbc

import SQL_Queries


load_dotenv()

DRIVER = os.getenv('MS_SQL_DRIVER')
SERVER = os.getenv('MS_SQL_SERVER')
WORK_DATABASE = os.getenv('MS_SQL_DATABASE')
PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

"""Simple Connection"""
# connection_string = f'''DRIVER={{SQL SERVER}};
#                  SERVER={SERVER};
#                  DATABASE={PAD_DATABASE};
#                  Trusted_Connection=yes'''

"""Secure Connection"""
connection_string = f'''DRIVER={DRIVER};
                 SERVER={SERVER};
                 DATABASE={PAD_DATABASE};
                 UID={USER};
                 PWD={PASSWORD}'''
                 
conn = pyodbc.connect(connection_string)
conn.autocommit = True


# создание базы данных через vscode
try:
    SQL_QUERY = SQL_Queries.create_database_default(WORK_DATABASE)
    conn.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'Database {WORK_DATABASE} Created')
# finally:
#     conn.close()


cursor = conn.cursor()
table_name = 'Products'


# создание таблицы
try:
    SQL_QUERY = SQL_Queries.create_table('Products')
    cursor.execute(fr'USE{WORK_DATABASE};')
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'Table {table_name} Created')
# finally:
#     conn.close()    
    

# заполнение таблицы данными
try:
    SQL_QUERY = SQL_Queries.insert_data_products(table_name)
    cursor.execute(fr'USE {WORK_DATABASE};')
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    print(f'Data in {table_name} Inserted')
# finally:
#     conn.close()
    
    
data_list = []

# получаем данные из таблицы
try:
    SQL_QUERY = SQL_Queries.get_data(table_name)
    cursor.execute(fr'USE {WORK_DATABASE};')
    result = cursor.execute(SQL_QUERY)
except pyodbc.Error as ex:
    print(ex)
else:
    records = result.fetchall()
    for record in records:
        data_dict = {'id': record.ProductId, 'name': record.ProductName, 'price': float(record.Price)}
        data_list.append(data_dict)
finally:
    conn.close()
    
with open('data_products.json', 'w', encoding='utf-8') as fp:
    json.dump(data_list, fp, ensure_ascii=False, indent=4)
    print('Data Added to json file')