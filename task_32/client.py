import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    while True:
        message = input("Введите сообщение (или 'exit' для отключения): ")
        if message == 'exit':
            client.send(message.encode('utf-8'))
            print("Вы отключились от сервера.")
            break
        elif message.strip() == '':
            print("Пустое сообщение, попробуйте снова.")
            continue
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Ответ от сервера: {response}")

    client.close()

if __name__ == "__main__":
    start_client()