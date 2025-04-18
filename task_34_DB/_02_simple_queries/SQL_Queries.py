def create_database_default(name):
    COMMAND = fr'CREATE DATA BASE {name};'
    return COMMAND


def create_table(name):
    COMMAND = fr'''CREATE TABLE {name};
                    (ProductID INT PRIMARY KEY,
                    ProductName nvarchar(50)
                    Price money)'''
    return COMMAND


def insert_data_products(name):
    COMMAND = fr"""INSERT INTO {name} (ProductId, ProductName, Price)
                    VALUES
                    (1, 'Desktop Computer', 800),
                    (2, 'Laptop', 1200),
                    (3, 'Table', 200),
                    (4, 'Monitor', 350),
                    (5, 'Printer', 150);"""
    return COMMAND


def get_data(name):
    COMMAND = fr"""SELECT ProductId, Productname, Price
                    FROM {name};"""
    return COMMAND