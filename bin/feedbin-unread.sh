#!/usr/bin/env bash

[[ -z "$FEEDBIN_KEY" ]] && exit

reply="$(curl -u "$FEEDBIN_KEY" \
	https://api.feedbin.me/v2/unread_entries.json \
	2>/dev/null | jq length)"

echo " $reply"

