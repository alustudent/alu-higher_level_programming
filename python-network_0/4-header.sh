#!/bin/bash
# Sends a GET request with the header X-HolbertonSchool-User-Id: 98 and displays the body
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
