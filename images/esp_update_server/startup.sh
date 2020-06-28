#!/usr/bin/env bash

python3 wait_services.py

FILE=~/initializaed_flag
if [ ! -f "$FILE" ]; then
    ~/init.sh
    touch "$FILE"
fi

python3 manage.py makemigrations
python3 manage.py migrate
