#!/usr/bin/env bash

[[ -z "$OPENWEATHERMAP_KEY" || -z "$1" ]] && exit 1

url="http://api.openweathermap.org/data/2.5/weather?q=${1}&units=metric&APPID=${OPENWEATHERMAP_KEY}"
reply="$(curl "$url" 2>/dev/null | jq -e .main.temp)"

[[ $? -eq 0 ]] && echo " $reply℃"
