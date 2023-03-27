import socket, threading

HOST, PORT = ('', 10500)



def start_new_connection_answer(conn, host):
    pass


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(HOST, PORT)
server.listen()


while True:
    conn, host = server.accept()
    
