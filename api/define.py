from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        url_components = parse.urlsplit(url)
        # print (f"the url components are{url_components}")
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        dictionary_api_url = "https://restcountries.com/v3.1/name/"

        # print(dictionary)
        if 'country' in dictionary:

            response = requests.get(dictionary_api_url + dictionary["country"])
            data = response.json()
            capital = data[0]['capital'][0]
            message = f"The capital of {dictionary['country']} is {capital}"

        elif 'capital' in dictionary:
            
            response = requests.get(dictionary_api_url + dictionary["capital"])
            data = response.json()
            country = data[0]['name']['common']
            message = f"The capital of {dictionary['capital']} is {country}"

        else:
            message = "Invalid request, please try another request"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(message.encode())









if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()