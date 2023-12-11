#!/bin/bash


if command -v docker-compose &> /dev/null; then
    echo "Docker Compose уже установлен."
else
    # Установка Docker Compose
    echo "Установка Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "Docker Compose успешно установлен."
fi

docker-compose up -d
echo "http://172.19.0.5:3000/"
