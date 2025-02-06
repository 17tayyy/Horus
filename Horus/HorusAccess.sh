#!/bin/bash

USER_NAME=$(whoami)

if [[ "$USER_NAME" == "tay" ]]; then
    echo "Welcome, $USER_NAME. No redirection for you."
    exec /bin/zsh
    exit 0
fi

if [[ "$USER_NAME" == "user" ]]; then
    cd /opt/Horus
    exec python3 /opt/Horus/Horus.py
    exit 0
fi

echo "Welcome, $USER_NAME. Starting default shell."
exec /bin/bash 
