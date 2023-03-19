from socketserver import TCPServer, BaseRequestHandler

class WebHandler(BaseRequestHandler):

    def handle(self) -> None:
        # HTTP_head = 'HTTP/1.1 200 OK \r\n'
        # HTTP_type = 'Content-Type: text\html; charset=utf-8\r\n\r\n'
        HDRS = 'HTTP/1.1 200 OK \r\nContent-Type: text\html; charset=utf-8\r\n\r\n'
        self.data = self.request.recv(1024).strip()
        print(f'{self.client_address[0]} подключился')
        print(self.data.decode('utf-8'), 'Получены данные')
        # heading = HTTP_head+HTTP_type
        html_page = ''
        with open('page.html','r+', encoding='utf-8') as new_page:
            content = new_page.read()
        self.request.send(HDRS.encode('utf-8')+content.encode('utf-8'))


if __name__ == '__main__':
    with TCPServer(('',10500) ,WebHandler) as webserver:
        webserver.serve_forever()