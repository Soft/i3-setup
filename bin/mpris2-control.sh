#!/usr/bin/env bash

players=( lollypop clementine spotify )

for p in "${players[@]}"; do
	pidof $p >& /dev/null
	if [ $? -eq 0 ]; then
		target=$p
		break
	fi
done

if [ -z ${target+x} ]; then
	exit
fi

case "$1" in
	toggle) method=PlayPause ;;
	next) method=Next ;;
	prev) method=Previous ;;
	stop) method=Stop ;;
	*) exit 1 ;;
esac

dbus-send --print-reply \
		  --dest=org.mpris.MediaPlayer2.$target \
		  /org/mpris/MediaPlayer2 \
		  org.mpris.MediaPlayer2.Player.$method

