def write_text_to_file(filename):
    text = """Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

filename = 'text_file.txt'
write_text_to_file(filename)  # Записываем текст в файл
read_text_from_file(filename)  # Читаем текст из файла и выводим его в консоль