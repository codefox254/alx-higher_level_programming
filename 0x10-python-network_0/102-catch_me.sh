#!/bin/bash
#this script causes server response "you got me"
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me | grep 'You find me!'
