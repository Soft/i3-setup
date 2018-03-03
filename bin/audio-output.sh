#!/usr/bin/env bash

CARD="$1"
CURRENT="$(ponymix -c "$CARD" get-profile)"

if [[ "$CURRENT" == "output:iec958-stereo" ]]; then
    echo ""
else
    echo ""
fi
