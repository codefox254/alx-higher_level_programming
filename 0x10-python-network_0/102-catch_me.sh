#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me
response=$(curl -sL -X GET 0.0.0.0:5000/catch_me)
if [[ "$response" == *"You find me!"* ]]; then
    echo "Success! The server responded with the expected message."
else
    echo "Unexpected response from the server."
fi
