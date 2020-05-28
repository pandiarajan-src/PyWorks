'''Learn HTTP requests from this sample'''
import json
import requests

class MyHTTPDisplay:
    """This class does HTTP display operations"""
    def __init__(self):
        """Initialize basic constants"""
        self.http_json_key_names = ["id", "brand", "model", "production_year", "convertible"]
        self.http_display_width = [10, 15, 10, 20, 15]

    def display_headers(self):
        """Display table headers with key names and display width"""
        for(header_name, header_width) in zip(self.http_json_key_names, self.http_display_width):
            print(header_name.ljust(header_width), end='| ')
        print()

    def display_contents(self, content):
        """Display HTTP JSON contents in the table format"""
        for(header_name, header_width) in zip(self.http_json_key_names, self.http_display_width):
            print(str(content[header_name]).ljust(header_width), end='| ')
        print()

    def display_empty(self):
        """Display HTTP empty contents in the table format"""
        for header_width in self.http_display_width:
            print("".ljust(header_width), end='| ')
        print()

    def display(self, json_content):
        """Display http json content as table"""
        print(sum(self.http_display_width)*"-")
        self.display_headers()
        if isinstance(json_content, list):
            for content in json_content:
                self.display_contents(content)
        elif isinstance(json_content, dict):
            if json_content:
                self.display_contents(json_content)
            else:
                self.display_empty()
        print(sum(self.http_display_width)*"-")


class MyHTTPRequest:
    """This class does HTTP basic CRUD operations"""
    time_out = 2
    @staticmethod
    def get_request(request_content, headers=None):
        """HTTP Get Request to process JSON server request"""
        try:
            if headers:
                reply = requests.get(request_content, headers=headers, \
                                        timeout=MyHTTPRequest.time_out)
            else:
                reply = requests.get(request_content, timeout=MyHTTPRequest.time_out)
        except requests.RequestException as ex:
            print("Request exception occured {0}".format(str(ex)))
        else:
            MyHTTPRequest.check_display_reply_content(reply)


    @staticmethod
    def post_request(request_content, post_content):
        """HTTP POST Request to send JSON content to server"""
        try:
            h_content = {'Content-Type': 'application/json'}
            reply = requests.post(request_content, headers=h_content, \
                                    data=json.dumps(post_content), \
                                    timeout=MyHTTPRequest.time_out)
        except requests.RequestException as ex:
            print("Request exception occured {0}".format(str(ex)))
        else:
            MyHTTPRequest.check_display_reply_content(reply)

    @staticmethod
    def delete_request(request_content):
        """HTTP Delete Request to delete a record in JSON server"""
        try:
            reply = requests.delete(request_content, timeout=MyHTTPRequest.time_out)
        except requests.RequestException as ex:
            print("Request exception occured {0}".format(str(ex)))
        else:
            MyHTTPRequest.check_display_reply_content(reply)

    @staticmethod
    def put_request(request_content, put_content):
        """HTTP PUT Request to update a JSON record"""
        try:
            h_content = {'Content-Type': 'application/json'}
            reply = requests.put(request_content, headers=h_content, \
                                 data=json.dumps(put_content), \
                                 timeout=MyHTTPRequest.time_out)
        except requests.RequestException as ex:
            print("Request exception occured {0}".format(str(ex)))
        else:
            MyHTTPRequest.check_display_reply_content(reply)

    @staticmethod
    def check_display_reply_content(reply):
        """HTTP reply status is verified here and contents were displayed properly"""
        if reply.status_code == requests.codes['ok']:
            MyHTTPDisplay().display(reply.json())
        elif reply.status_code == requests.codes['not_found']:
            print("HTTP requests code not found, it means resource is not available")
        else:
            print("HTTP error code returned {0}".format(str(reply.status_code)))



if __name__ == "__main__":
    try:
        print("*****************HTTP GET Request*******************\n")
        MyHTTPRequest().get_request("http://localhost:3000/cars")
        MyHTTPRequest().get_request("http://localhost:3000/cars/2")
        MyHTTPRequest().get_request("http://localhost:3000/cars?_sort=production_year")
        MyHTTPRequest().get_request("http://localhost:3000/cars?_sort=production_year&_order=desc")

        print("\n*****************HTTP POST Request*******************\n")
        H_CLOSE = {'Connection': 'Close'}
        POST_DATA = {'id': 8,
                     'brand': 'Porsche',
                     'model': '911',
                     'production_year': 1963,
                     'convertible': False}
        MyHTTPRequest().post_request("http://localhost:3000/cars", POST_DATA)
        MyHTTPRequest().get_request("http://localhost:3000/cars", headers=H_CLOSE)

        print("\n*****************HTTP DELETE Request*******************\n")
        MyHTTPRequest().delete_request("http://localhost:3000/cars/4")
        MyHTTPRequest().get_request("http://localhost:3000/cars", headers=H_CLOSE)

        print("\n*****************HTTP PUT Request*******************\n")
        PUT_DATA = {'id': 6,
                    'brand': 'Mercedes Benz',
                    'model': '300SL',
                    'production_year': 1967,
                    'convertible': True}
        MyHTTPRequest().put_request("http://localhost:3000/cars/6", PUT_DATA)
        MyHTTPRequest().get_request("http://localhost:3000/cars", headers=H_CLOSE)
    except Exception as ex:#pylint: disable=broad-except
        print("Unknown Exception occured {0}".format(str(ex)))
