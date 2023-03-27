import socket
from threading import Thread

HOST, PORT = ('', 10500)



def start_new_connection_answer(conn, host):
    data = conn.recv(1024)
    if not data:
        conn.close()
    else:
        print(f'{host} подключился')
        print('Получены данные',data.decode('utf-8'))
        HDRS = 'HTTP/1.1 200 OK \r\nContent-Type: text\html; charset=utf-8\r\n\r\n'
        # content = '<html lang="ru"> <head> <meta charset="UTF-8"></head><p>Тестовая страница</p> </html>'
        content = '<html lang="ru"> <p>Тестовая страница</p> </html>'
        # conn.send(HDRS.encode('utf-8')+content.encode('utf-8')) 
        conn.send(HDRS.encode('utf-8')+content.encode('utf-8'))
    conn.close()




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


while True:
    conn, host = server.accept()
    new_connectiton = Thread(target=start_new_connection_answer(conn, host))
    new_connectiton.daemon = True
    new_connectiton.start()