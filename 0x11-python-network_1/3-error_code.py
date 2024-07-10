#!/usr/bin/python3
"""A Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
        print(body)
    except urllib.error.HTTPerror as httperr:
        print(f'Error code:', {e.code})
