#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
curl -s -o /tmp/response.txt $1; status_code=$(grep -oE '[0-9]{3}' /tmp/response.txt); rm /tmp/response.txt; echo $status_code
