#!/bin/bash

if [ -d "new_folder" ]; then
    mkdir if_nilo
    echo "if_nilo folder created"
else
    echo "new_folder does not exist"
fi

if [ -d "if_nilo" ]; then
    mkdir "hyperionDev"
    echo "hyperionDev folder created"
else
    mkdir "django-projects"
    echo "if_nilo does not exist, creating django-projects instead"
fi
