#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200
response=$(curl -s -o /tmp/response.txt -w "%{http_code}" $1); status_code=$(tail -c 3 <<< $response); if [ $status_code -eq 200 ]; then cat /tmp/response.txt; fi
