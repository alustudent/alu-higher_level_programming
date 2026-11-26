#!/usr/bin/python3
"""Sends a POST request with an email to a URL and displays the body."""
import sys
import requests

if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={"email": sys.argv[2]}).text)
