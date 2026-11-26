#!/bin/bash
# Sends a GET request with the header X-School-User-Id: 98 and displays the body
curl -sH "X-School-User-Id: 98" "$1"
