#!/usr/bin/python3
"""Takes in a url
   sends a request to the URL and displays the value of the
   X-Request-Id variable found in the header of the response.
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv
    result = request.Request(argv[1])
    with request.urlopen(result) as a:
        print(a.headers.get('X-Request-Id'))
