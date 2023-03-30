from socketserver import TCPServer, BaseRequestHandler, ThreadingTCPServer
import urllib3


class WebHandler(BaseRequestHandler):

    def handle(self) -> None:       
        
        self.data = self.request.recv(1024).decode('utf-8')
        print(f'{self.client_address[0]} подключился')       
        return_data = ReturnPageWithHTTPRequest(self.data)       
        self.request.send(return_data)

def hdrs(status_line:str):
    http = 'HTTP/1.1'
    content_type = 'Content-Type: text\html; charset=utf-8\r\n\r\n'
    if status_line == '200':
        status_query =' '.join([status_line,'OK'])
    else:
        status_query =' '.join([status_line,'Not Found'])

    return ' '.join([http,status_query+content_type,'\r\n'])         
          


def return_page_query(data):
     parsing_string = data.split('\r\n')
     first_head = parsing_string[0]    
     page = first_head.split()[1]
     return page

def ReturnPageWithHTTPRequest(data):
    content = None    
    HDRS = None
    page = return_page_query(data)
    if page == '/':
        HDRS = hdrs('200')
        with open('pages/index.html','r+', encoding='utf-8') as new_page:
                content = new_page.read()
    else:
         HDRS = hdrs('404')
         content = '<html lang="ru"> <head> <meta charset="UTF-8"></head><p>404 страница не найдена</p> </html>'
        
    return HDRS.encode('utf-8')+content.encode('utf-8')



if __name__ == '__main__':
    try:
        serv_web = ThreadingTCPServer(('',10500) ,WebHandler)
        serv_web.serve_forever()
    except KeyboardInterrupt:
        serv_web.server_close()

    
    