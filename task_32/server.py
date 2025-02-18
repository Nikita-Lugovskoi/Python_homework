import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Клиент отключился.")
                break
            if message == 'exit':
                print("Клиент запросил отключение.")
                break
            print(f"Получено сообщение: {message}")
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Сервер запущен и ожидает подключения...")

    while True:
        client_socket, addr = server.accept()
        print(f"Подключен клиент: {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()