#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        request = response.read()
    print("Body response:")
    print(f"\t- type: {type(request)}")
    print(f"\t- content: {request}")
