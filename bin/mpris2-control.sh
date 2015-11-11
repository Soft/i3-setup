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

function control {
	dbus-send --print-reply \
		--dest=org.mpris.MediaPlayer2.$target \
		/org/mpris/MediaPlayer2 \
		org.mpris.MediaPlayer2.Player.$1 2> /dev/null
}

function get-metadata {
	dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.$target \
			/org/mpris/MediaPlayer2 \org.freedesktop.DBus.Properties.Get \
			string:"org.mpris.MediaPlayer2.Player" \
			string:"Metadata" 2> /dev/null
}

function find-value {
	grep -A1 "^$1$" <<< "$2" | tail -n1
}

function find-strings {
	grep -oP '(?<=").*(?=")' <<< "$1"
}

function info {
	reply=$(get-metadata spotify)
	[[ -z "$reply" ]] && exit

	strings=$(find-strings "$reply")

	artist=$(find-value "xesam:artist" "$strings")
	song=$(find-value "xesam:title" "$strings")

	[[ ! "$artist"  =~ ^xesam: ]] && echo " $artist - $song" | sed "s/\"/\\\\\"/g"
}

case "$1" in
	toggle) control "PlayPause" ;;
	next) control "Next" ;;
	prev) control "Previous" ;;
	stop) control "Stop" ;;
	info) info ;;
	*) exit 1 ;;
esac
