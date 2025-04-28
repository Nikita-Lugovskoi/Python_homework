import os

from dotenv import load_dotenv
import pyodbc
import csv

import SQL_Queries

class ConnectDB:
    @classmethod
    def connect_to_db(cls, driver, server, pad_database, user, password):
        connection_string = f'''DRIVER={driver};
                                SERVER={server};
                                DATABASE={pad_database};
                                UID={user};
                                PWD={password}'''
        try:
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True
            return conn
        except pyodbc.ProgrammingError as ex:
            print(ex)
        return None
    
class NorthWindData:
    
    def __init__(self, conn_obj, database_name):
        self.conn = conn_obj
        self.database_name = database_name
        self.cursor = self.conn.cursor()
    
    # создание базы данных    
    def create_database_default(self, database_name):
        try:
            SQL_QUERY = SQL_Queries.create_database_default(database_name)
            self.conn.execute(SQL_QUERY)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print(f'База данных {database_name} создана!')
            
    # создание таблицы customers_data        
    def create_table_customers_data(self, table_name, database_name):
        try:
            SQL_QUERY = SQL_Queries.create_table_customers_data(table_name)
            self.cursor.execute(fr'USE {database_name};')
            self.cursor.execute(SQL_QUERY)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print(f'Таблица {table_name} создана!')    

    # создание таблицы employees_data 
    def create_table_employees_data(self, table_name, database_name):
        try:
            SQL_QUERY = SQL_Queries.create_table_employees_data(table_name)
            self.cursor.execute(fr'USE {database_name};')
            self.cursor.execute(SQL_QUERY)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print(f'Таблица {table_name} создана!') 
            
    # создание таблицы orders_data 
    def create_table_orders_data(self, table_name, database_name):
        try:
            SQL_QUERY = SQL_Queries.create_table_orders_data(table_name)
            self.cursor.execute(fr'USE {database_name};')
            self.cursor.execute(SQL_QUERY)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print(f'Таблица {table_name} создана!')
            
    # Загружает данные клиентов из CSV файла.           
    def load_customers(self, csv_file):
            try:
                with open(csv_file, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    cursor = self.conn.cursor()
                    for row in reader:
                        cursor.execute('''
                        INSERT INTO customers_data (customer_id, company_name, contact_name)
                        VALUES (?, ?, ?)
                        ''', (row['customer_id'], row['company_name'], row['contact_name']))
            except pyodbc.ProgrammingError as PEex:
                print(PEex)
            except pyodbc.IntegrityError as IEex:
                print(IEex)
            else:
                print(f'Данные добавлены в таблицу {'customers_data'}!')
                
    # Загружает данные сотрудников из CSV файла.
    def load_employees(self, csv_file):
        try:   
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                cursor = self.conn.cursor()
                for employee_id, row in enumerate(reader, start=1):
                    cursor.execute('''
                    INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_data, notes)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''', (employee_id, row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']))
        except pyodbc.ProgrammingError as PEex:
            print(PEex)
        except pyodbc.IntegrityError as IEex:
            print(IEex)
        else:
            print(f'Данные добавлены в таблицу {'employees_data'}!')
    
    # Загружает данные заказов из CSV файла.                
    def load_orders(self, csv_file):
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                cursor = self.conn.cursor()
                for row in reader:
                    cursor.execute('''
                    INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))
        except pyodbc.ProgrammingError as PEex:
            print(PEex)
        except pyodbc.IntegrityError as IEex:
            print(IEex)
        else:
            print(f'Данные добавлены в таблицу {'orders_data'}!')
                  
            

if __name__ == '__main__':
    load_dotenv()
    DRIVER = os.getenv('MS_SQL_DRIVER')
    SERVER = os.getenv('MS_SQL_SERVER')
    WORK_DATABASE = "NorthWind"
    PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')
    
    my_conn = ConnectDB.connect_to_db(DRIVER, SERVER, PAD_DATABASE, USER, PASSWORD)
    my_manager = NorthWindData(my_conn, WORK_DATABASE)
    
    my_manager.create_database_default(WORK_DATABASE)
    my_manager.create_table_customers_data('customers_data', WORK_DATABASE)
    my_manager.create_table_employees_data('employees_data', WORK_DATABASE)
    my_manager.create_table_orders_data('orders_data', WORK_DATABASE)
    
    my_manager.load_customers('module\\customers_data.csv')
    my_manager.load_employees('module\\employees_data.csv')
    my_manager.load_orders('module\\orders_data.csv')
    