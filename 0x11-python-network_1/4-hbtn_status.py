#!/usr/bin/python3
"""A Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    request = response.content
    print("Body response:")
    print(f"\t- type: {type(request)}")
    print(f"\t- content: {request}")
