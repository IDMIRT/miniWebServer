from socketserver import TCPServer, BaseRequestHandler, ThreadingTCPServer
import urllib3
# from _thread import start_new_thread

# class ThreadingTCPServer()


class WebHandler(BaseRequestHandler):

    def handle(self) -> None:       
        
        self.data = self.request.recv(1024).decode('utf-8')
        print(f'{self.client_address[0]} подключился')
        # print(self.data.decode('utf-8'), 'Получены данные')
        return_data = ReturnPageWithHTTPRequest(self.data)
        # with open('page.html','r+', encoding='utf-8') as new_page:
            # content = new_page.read()
        # self.request.send(HDRS.dataencode('utf-8')+content.encode('utf-8'))
        self.request.send(return_data)

def hdrs(status_line:str):
    http = 'HTTP/1.1'
    if status_line == '200':
        status_query =' '.join([status_line,'OK'])
    else:
        status_query =' '.join([status_line,'Not Found'])

    return ' '.join([http,status_query,'\r\n'])         
          


def return_page_query(data):
     parsing_string = data.split('\r\n')
     first_head = parsing_string[0]
    #  type_query = first_head.split()[0]
     page = first_head.split()[1]
     return page

def ReturnPageWithHTTPRequest(data):
    content = None
    content_type = 'Content-Type: text\html; charset=utf-8\r\n\r\n'
    HDRS = None#hdrs('200')+content_type#'HTTP/1.1 200 OK \r\nContent-Type: text\html; charset=utf-8\r\n\r\n'
    page = return_page_query(data)
    if page == '/':
        HDRS = hdrs('200')+content_type
        with open('pages/index.html','r+', encoding='utf-8') as new_page:
                content = new_page.read()
    else:
         HDRS = hdrs('404')+content_type
         with open('pages/notfound.html','r+', encoding='utf-8') as new_page:
                content = new_page.read()
        
    return HDRS.encode('utf-8')+content.encode('utf-8')



if __name__ == '__main__':
    try:
        serv_web = ThreadingTCPServer(('',10500) ,WebHandler)
        serv_web.serve_forever()
    except KeyboardInterrupt:
        serv_web.server_close()

    
    