#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv
    d = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    r = request. Request(argv[1], data)
    with request.urlopen(r) as a:
        print(a.read(). decode('urf-8'))
