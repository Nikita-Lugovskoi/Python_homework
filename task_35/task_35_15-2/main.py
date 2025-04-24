import os

import pyodbc
from dotenv import load_dotenv
import json
import time
from datetime import datetime

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
        
        
class HospitalData:
    
    def __init__(self, conn_obj):
        self.conn = conn_obj
        self.cursor = self.conn.cursor()
        
    def save_to_json(self, data, filename):
        json_path = os.path.join('task_36_15-2', 'json_data', filename)
        with open(json_path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        

class HospitalDatabase(HospitalData):
    
    def __init__(self, conn_obj, database_name):
        super().__init__(conn_obj)
        self.database_name = database_name
        
    def check_exists(self, table_name):
        check_exists_data_list = []
        try:
            SQL_QUERY = SQL_Queries.exists_doctors(table_name)
            self.cursor.execute(fr'USE {self.database_name};')
            result = self.cursor.execute(SQL_QUERY)
            records = result.fetchall()
            for record in records:
                data_dict = {
                    'Surname': record.Surname, 
                    'Name': record.Name, 
                    'Salary': float(record.Salary),
                    'Premium': float(record.Premium)
                    }
                check_exists_data_list.append(data_dict)
        except pyodbc.Error as ex:
            print(f"Error checking exists: {ex}")
            # [print(data) for data in check_exists_data_list]
        return check_exists_data_list


    
    def check_any_doctors(self, table_name, Ward_Id):
        check_any_doctors_list = []
        try:
            SQL_QUERY = SQL_Queries.exists_doctor_for_ward(table_name, Ward_Id)
            self.cursor.execute(fr'USE {self.database_name};')
            result = self.cursor.execute(SQL_QUERY)
            records = result.fetchall()
            for record in records:
                data_dict = {
                    'Surname': record.Surname, 
                    'Name': record.Name, 
                    'Salary': float(record.Salary),
                    'Premium': float(record.Premium)
                    }
                check_any_doctors_list.append(data_dict)
        except pyodbc.Error as ex:
            print(ex)
        # [print(data) for data in check_any_doctors_list]
        return check_any_doctors_list

            
    def check_some_doctors(self, table_name, StartTime, EndTime):
        check_some_doctors_list = []
        try:
            SQL_QUERY = SQL_Queries.exists_doctor_for_exam_time(table_name, StartTime, EndTime)
            self.cursor.execute(fr'USE {self.database_name};')
            result = self.cursor.execute(SQL_QUERY)
            records = result.fetchall()
            for record in records:
                data_dict = {
                    'Surname': record.Surname, 
                    'Name': record.Name, 
                    'Salary': float(record.Salary),
                    'Premium': float(record.Premium)
                    }
                check_some_doctors_list.append(data_dict)
        except pyodbc.Error as ex:
            print(ex)
        # [print(data) for data in check_some_doctors_list]            
        return check_some_doctors_list
    
    
    def check_all_doctors(self):
        check_all_doctors_list = []
        try:
            SQL_QUERY = SQL_Queries.select_doctor_for_all_wardId()
            self.cursor.execute(fr'USE {self.database_name};')
            result = self.cursor.execute(SQL_QUERY)
            records = result.fetchall()
            for record in records:
                data_dict = {
                    'Surname': record.Surname, 
                    'Name': record.Name, 
                    'WardId': record.WardId
                    }
                check_all_doctors_list.append(data_dict)
        except pyodbc.Error as ex:
            print(ex)
        # [print(data) for data in check_all_doctors_list]            
        return check_all_doctors_list
    
    
    def check_unoin_doctors(self, table_name):
        check_unoin_doctors_list = []
        try:
            SQL_QUERY = SQL_Queries.select_union_doctors(table_name)
            self.cursor.execute(fr'USE {self.database_name};')
            result = self.cursor.execute(SQL_QUERY)
            records = result.fetchall()
            for record in records:
                data_dict = {
                    'FullName': record.Fullname, 
                    'Salary': float(record.Salary)
                    }
                check_unoin_doctors_list.append(data_dict)
        except pyodbc.Error as ex:
            print(ex)
        # [print(data) for data in check_unoin_doctors_list]            
        return check_unoin_doctors_list
 
 
    def check_all_unoin_doctors(self, table_name):
            check_all_unoin_doctors_list = []
            try:
                SQL_QUERY = SQL_Queries.select_all_union_doctors(table_name)
                self.cursor.execute(fr'USE {self.database_name};')
                result = self.cursor.execute(SQL_QUERY)
                records = result.fetchall()
                for record in records:
                    data_dict = {
                        'Result': record.Result, 
                        'Number of Doctors': record.Number_of_Doctors
                        }
                    check_all_unoin_doctors_list.append(data_dict)
            except pyodbc.Error as ex:
                print(ex)
            # [print(data) for data in check_all_unoin_doctors_list]            
            return check_all_unoin_doctors_list
        
        
    def check_join_info_about_doctors(self):
            check_join_info_about_doctors = []
            try:
                SQL_QUERY = SQL_Queries.join_info_about_doctors()
                self.cursor.execute(fr'USE {self.database_name};')
                result = self.cursor.execute(SQL_QUERY)
                records = result.fetchall()
                for record in records:
                    
                    data_dict = {
                        'Surname': record.Surname, 
                        'Name': record.Name, 
                        'Ward': record.Ward,
                        'Departament': record.Departament
                        }
                    check_join_info_about_doctors.append(data_dict)
            except pyodbc.Error as ex:
                print(ex)
            # [print(data) for data in check_join_info_about_doctors]            
            return check_join_info_about_doctors        
            
      
if __name__ == '__main__':
    load_dotenv()
    DRIVER = os.getenv('MS_SQL_DRIVER')
    SERVER = os.getenv('MS_SQL_SERVER')
    WORK_DATABASE = "Hospital"
    PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')
    
    my_conn = ConnectDB.connect_to_db(DRIVER, SERVER, PAD_DATABASE, USER, PASSWORD)
    my_manager = HospitalDatabase(my_conn, WORK_DATABASE)
    
    # получаем данные из таблицы Doctors
    exists_result = my_manager.check_exists('Doctors')
    result_any_doctors = my_manager.check_any_doctors('Doctors', '3')
    result_some_doctors = my_manager.check_some_doctors('Doctors', '13:00:00', '12:50:00')
    result_all_doctors = my_manager.check_all_doctors()
    result_union_doctors = my_manager.check_unoin_doctors('Doctors')
    result_all_union_doctors = my_manager.check_all_unoin_doctors('Doctors')
    result_all_union_doctors = my_manager.check_join_info_about_doctors()
    
    # сохраняем данные из таблицы Doctors в json файл
    my_manager.save_to_json(exists_result, 'data_exists_doctors.json')
    my_manager.save_to_json(result_any_doctors, 'data_any_doctors.json')
    my_manager.save_to_json(result_some_doctors, 'data_some_doctors.json')
    my_manager.save_to_json(result_all_doctors, 'data_all_doctors.json')
    my_manager.save_to_json(result_union_doctors, 'data_union_doctors.json')
    my_manager.save_to_json(result_all_union_doctors, 'data_all_union_doctors.json')    
    my_manager.save_to_json(result_all_union_doctors, 'data_about_join_doctors.json')    