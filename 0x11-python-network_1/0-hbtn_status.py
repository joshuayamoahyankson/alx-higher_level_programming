#!/usr/bin/python3
"""A module to fetch information from a URL"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
