#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton servers
curl -s -L -X PUT -d "user_id=1650" -H "Origin: You got me!" 0.0.0.0:5000/catch_me
