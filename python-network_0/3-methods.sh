#!/bin/bash
# Displays all HTTP methods the server of a URL accepts
curl -sI "$1" | grep -i "^Allow:" | cut -d " " -f 2- | tr -d "\r"
