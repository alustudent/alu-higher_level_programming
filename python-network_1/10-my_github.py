#!/usr/bin/python3
"""Displays your GitHub user id, using Basic Auth with a token."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    print(response.json().get("id"))
