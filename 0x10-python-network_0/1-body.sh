#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response if the status
[ "$status_code" -eq 200 ] && curl -s $1
