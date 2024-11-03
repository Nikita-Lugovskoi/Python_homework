# *args
def sum_of_numbers(*args):
    return sum(args)

result = sum_of_numbers(10, 11, 12, 13, 14, 15)
print(result)

# **kwargs
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
info(name = "Nikita", age = 25, country = "Russia")

# *args **kwargs
def mixed_arguments(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mixed_arguments(1, 2, 3, name="Bob", age=25)
