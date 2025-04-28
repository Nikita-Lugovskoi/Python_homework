# создание базы данных    
def create_database_default(name):
    COMMAND = fr'CREATE DATABASE {name};'
    return COMMAND

# создание таблицы customers_data    
def create_table_customers_data(name):
    COMMAND = fr'''CREATE TABLE {name}
                    (customer_id NVARCHAR(10) PRIMARY KEY,
                    company_name NVARCHAR(100) NOT NULL,
                    contact_name NVARCHAR(50) NOT NULL)'''
    return COMMAND

# создание таблицы employees_data    
def create_table_employees_data(name):
    COMMAND = fr'''CREATE TABLE {name}
                    (employee_id INT PRIMARY KEY,
                    first_name NVARCHAR(100) NOT NULL,
                    last_name NVARCHAR(100) NOT NULL,
                    title NVARCHAR(100) NOT NULL,
                    birth_data DATE NOT NULL,
                    notes NVARCHAR(1000) NOT NULL)'''
    return COMMAND

# создание таблицы orders_data    
def create_table_orders_data(name):
    COMMAND = fr'''CREATE TABLE {name}
                    (order_id INT PRIMARY KEY,
                    customer_id NVARCHAR(10) NOT NULL,
                    employee_id INT NOT NULL,
                    order_date DATE NOT NULL,
                    ship_city NVARCHAR(100) NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers_data(customer_id),
                    FOREIGN KEY (employee_id) REFERENCES employees_data(employee_id))'''
    return COMMAND
